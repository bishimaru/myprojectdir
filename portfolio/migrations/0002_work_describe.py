# Generated by Django 3.2.5 on 2021-09-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='describe',
            field=models.CharField(default=1, max_length=100, verbose_name='説明'),
            preserve_default=False,
        ),
    ]
