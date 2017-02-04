# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DELIVERY', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('mobile', models.CharField(max_length=16)),
                ('is_active', models.BooleanField(default=True)),
                ('credit', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='delivery_customer',
            name='commet',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='delivery_customer',
            name='mobile2',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='delivery_invoice',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='delivery_invoice',
            name='shipped_with',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DELIVERY.Shipping'),
        ),
    ]