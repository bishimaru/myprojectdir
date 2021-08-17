from django.contrib import admin
from .models import SlotData, TotalPay
from django.http.request import HttpRequest


class SlotDataAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'name', 'number', 'date', 'payout', 'memo')


class TotalPayAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'date', 'totalpay')


admin.site.register(SlotData, SlotDataAdmin)
admin.site.register(TotalPay, TotalPayAdmin)
