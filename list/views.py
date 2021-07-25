from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import SlotData, TotalPay
from django.db.models import Sum
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

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     name = self.request.GET.get('sn')
    #     totalpay = SlotData.objects.filter(
    #         store_name=name).aggregate(Sum('payout'))
    #     totalpay = totalpay['payout__sum']
    #     context['payout'] = totalpay
    #     return context

    def queryset(self):
        name = self.request.GET.get('sn')
        dates = TotalPay.objects.filter(
            store_name=name).distinct()
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
    #     global names
    #     store_name = self.request.GET.get('sn')
    #     date = self.request.GET.get('date')
    #     context = super().get_context_data()
    #     l = []
    #     for i in names:
    #         l.append(i)

    #     get = []
    #     for i in range(len(l)):

    #         totalpay = SlotData.objects.filter(
    #             store_name=store_name, date=date, name=l[i]['name']).aggregate(Sum('payout'))
    #         totalpay = totalpay['payout__sum']
    #         get.append(totalpay)

    #     context['test'] = totalpay
    #     return context


class DetailView(ListView):
    model = SlotData
    template_name = 'detail.html'

    def queryset(self):
        store_name = self.request.GET.get('sn')
        day = self.request.GET.get('date')
        name = self.request.GET.get('name')

        # d = (str)(date)
        # dte = datetime.datetime.strptime(d, '%Y%m%d')
        dates = SlotData.objects.filter(
            store_name=store_name, date=day, name=name)
        return dates
