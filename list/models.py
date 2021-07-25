from django.db import models
from datetime import datetime
from django.utils import timezone


class SlotData(models.Model):
    class Meta:
        db_table = 'data'
        verbose_name = "スロットデータ"
        verbose_name_plural = 'スロットデータ'

    store_name = models.CharField(max_length=100, verbose_name='店舗名')
    name = models.CharField(max_length=100, verbose_name='機種名')
    number = models.IntegerField(verbose_name='台番号')
    date = models.DateField(verbose_name='日付', default=timezone.now)
    bigbonus = models.IntegerField(verbose_name='BB')
    regularbonus = models.IntegerField(verbose_name='RB')
    count = models.IntegerField(verbose_name='総回転数')
    bbchance = models.CharField(max_length=10, verbose_name='BB確率')
    rbchance = models.CharField(max_length=10, verbose_name='RB確率')
    totalchance = models.CharField(max_length=10, verbose_name='合成確率')
    lastgames = models.IntegerField(verbose_name='宵越し')
    payout = models.IntegerField(verbose_name='差枚数')
    memo = models.CharField(
        max_length=50, verbose_name='メモ', blank=True, null=True)

    def __str__(self):
        return self.name


class TotalPay(models.Model):
    class Meta:
        db_table = 'totalpay'
        verbose_name = "差枚数"
        verbose_name_plural = '差枚数'

    store_name = models.CharField(max_length=100, verbose_name='店舗名')
    date = models.DateField(verbose_name='日付', default=timezone.now)
    totalpay = models.IntegerField(verbose_name='総差枚数')

    def __str__(self):
        return self.store_name
