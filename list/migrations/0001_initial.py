# Generated by Django 3.2.5 on 2021-07-25 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlotData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100, verbose_name='店舗名')),
                ('name', models.CharField(max_length=100, verbose_name='機種名')),
                ('number', models.IntegerField(verbose_name='台番号')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日付')),
                ('bigbonus', models.IntegerField(verbose_name='BB')),
                ('regularbonus', models.IntegerField(verbose_name='RB')),
                ('count', models.IntegerField(verbose_name='総回転数')),
                ('bbchance', models.CharField(max_length=10, verbose_name='BB確率')),
                ('rbchance', models.CharField(max_length=10, verbose_name='RB確率')),
                ('totalchance', models.CharField(max_length=10, verbose_name='合成確率')),
                ('lastgames', models.IntegerField(verbose_name='宵越し')),
                ('payout', models.IntegerField(verbose_name='差枚数')),
                ('memo', models.CharField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name': 'スロットデータ',
                'verbose_name_plural': 'スロットデータ',
                'db_table': 'data',
            },
        ),
        migrations.CreateModel(
            name='TotalPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100, verbose_name='店舗名')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日付')),
                ('totalpay', models.IntegerField(verbose_name='総差枚数')),
            ],
            options={
                'verbose_name': '差枚数',
                'verbose_name_plural': '差枚数',
                'db_table': 'totalpay',
            },
        ),
    ]
