# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 07:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DELIVERY', '0008_auto_20170204_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_invoice',
            name='shipping_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 4, 7, 40, 8, 664495)),
        ),
    ]