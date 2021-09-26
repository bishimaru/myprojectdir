from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import SlotData, TotalPay
from django.db.models import Sum, Avg, aggregates
import datetime
from django.db.models import Count, OuterRef, Subquery


class IndexView(TemplateView):
    template_name = 'index.html'


index = IndexView.as_view()


class StoreNameView(ListView):
    model = SlotData
    template_name = 'store_name.html'

    # SlotDataの全データを取得するメソッドを定義

    def queryset(self):
        return SlotData.objects.all().distinct().values("store_name")


class Vue(TemplateView):
    template_name = 'vue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'hello world'
        return context


vue = Vue.as_view()


class AllDisplayView(ListView):
    model = SlotData
    template_name = 'all_display.html'

    def queryset(self):
        store_name = self.request.GET.get('sn')
        all = SlotData.objects.filter(store_name=store_name)
        return all


class DateView(ListView):
    model = TotalPay
    template_name = 'date.html'

    def queryset(self):
        store_name = self.request.GET.get('sn')
        dates = TotalPay.objects.filter(
            store_name=store_name).distinct()
        dates = dates.order_by('-date')
        return dates


class NameView(ListView):
    model = SlotData
    template_name = 'name.html'
    context_object_name = 'name_cnt'

    def get_context_data(self, **kwargs):
        store_name = self.request.GET.get('sn')
        date = self.request.GET.get('date')
        context = super().get_context_data(**kwargs)

        nm = SlotData.objects.filter(
            store_name=store_name, date=date,).distinct().values('name')
        name_cnt = {}
        avarage = []
        name_pay = []

        for n in nm:
            cnt = SlotData.objects.filter(
                store_name=store_name, date=date, name=n['name']).values('name').count()
            name_cnt[n['name']] = cnt
        n_c = sorted(name_cnt.items(), key=lambda x: x[1], reverse=True)

        for n in n_c:

            ava = SlotData.objects.filter(
                store_name=store_name, date=date, name=n[0]).aggregate(Avg('count'))
            ava = int(ava['count__avg'])
            avarage.append(ava)

            py = SlotData.objects.filter(
                store_name=store_name, date=date, name=n[0]).aggregate(Sum('payout'))
            py = int(py['payout__sum'])
            name_pay.append(py)

        context.update({
            'name_cnt': n_c,
            'store_name': store_name,
            'date': date,
            'avg': avarage,
            'py': name_pay
        })
        return context

    def get_queryset(self):
        store_name = self.request.GET.get('sn')
        date = self.request.GET.get('date')

        a = SlotData.objects.filter(
            store_name=store_name, date=date).annotate(name_count=Avg('name'))
        names = SlotData.objects.filter(
            store_name=store_name, date=date,).distinct().values('store_name', 'name', 'date')

        return names

        # def get_context_data(self):

        # store_name = self.request.GET.get('sn')
        # date = self.request.GET.get('date')
        # context = super().get_context_data()
        # cnt = SlotData.objects.filter(
        #     store_name=store_name, date=date,
        # ).distinct().values('name').count()

        # context['cnt'] = cnt
        # return context


class DetailView(ListView):
    model = SlotData
    template_name = 'detail.html'

    def queryset(self):
        store_name = self.request.GET.get('sn')
        day = self.request.GET.get('date')
        name = self.request.GET.get('name')
        dates = SlotData.objects.filter(
            store_name=store_name, date=day, name=name)
        return dates

    def get_context_data(self):
        context = super().get_context_data()
        store_name = self.request.GET.get('sn')
        date = self.request.GET.get('date')
        name = self.request.GET.get('name')

        totalpay = SlotData.objects.filter(
            store_name=store_name, date=date, name=name).aggregate(Sum('payout'))
        totalpay = totalpay['payout__sum']

        avgpay = SlotData.objects.filter(
            store_name=store_name, date=date, name=name).aggregate(Avg('payout'))
        avgpay = (int)(avgpay['payout__avg'])

        avgcount = SlotData.objects.filter(
            store_name=store_name, date=date, name=name).aggregate(Avg('count'))
        avgcount = (int)(avgcount['count__avg'])

        context['tp'] = totalpay
        context['ap'] = avgpay
        context['ac'] = avgcount
        return context
