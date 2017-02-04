# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 07:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DELIVERY', '0004_auto_20170204_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_invoice',
            name='shipping_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 4, 7, 31, 15, 513569)),
        ),
        migrations.AlterField(
            model_name='delivery_customer',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='delivery_customer',
            name='mobile2',
            field=models.CharField(blank=True, default='', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='delivery_invoice',
            name='shipped_with',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DELIVERY.Shipping'),
        ),
    ]
