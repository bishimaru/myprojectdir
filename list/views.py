from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import SlotData, TotalPay
from django.db.models import Sum, Avg
import datetime


class IndexView(TemplateView):
    template_name = 'index.html'


index = IndexView.as_view()


class StoreNameView(ListView):
    model = SlotData
    template_name = 'store_name.html'

    # SlotDataの全データを取得するメソッドを定義

    def queryset(self):
        return SlotData.objects.all().distinct().values("store_name")


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

    names = []

    def get_queryset(self):
        store_name = self.request.GET.get('sn')
        date = self.request.GET.get('date')
        global names
        names = SlotData.objects.filter(
            store_name=store_name, date=date,).distinct().values('store_name', 'name', 'date')

        return names

    # def get_context_data(self):

    #     store_name = self.request.GET.get('sn')
    #     date = self.request.GET.get('date')
    #     context = super().get_context_data()
    #     cnt = SlotData.objects.filter(
    #         store_name=store_name, date=date,
    #     ).distinct().values('name').count()

    #     context['cnt'] = cnt
    #     return context


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
