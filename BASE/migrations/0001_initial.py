# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 09:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=512)),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Branch_Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BASE.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Branch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('comment', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Expense_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.FloatField(blank=True, null=True)),
                ('pic', models.FileField(default='', upload_to='')),
                ('stock_managed', models.BooleanField(default=False)),
                ('for_sale', models.BooleanField(default=False)),
                ('raw_material', models.BooleanField(default=False)),
                ('produced_item', models.BooleanField(default=False)),
                ('critical_stock', models.FloatField(default=0)),
                ('add_to_website', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='BASE.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='System_Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=64)),
                ('company_logo', models.FileField(upload_to='')),
                ('pos_from_stock', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Treasury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('comment', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(default='', max_length=16)),
                ('credit', models.FloatField(blank=True, default=0, null=True)),
                ('is_pos_employee', models.BooleanField(default=False)),
                ('is_pos_admin', models.BooleanField(default=False)),
                ('is_delivery_taker', models.BooleanField(default=False)),
                ('is_delivery_admin', models.BooleanField(default=False)),
                ('is_product_admin', models.BooleanField(default=False)),
                ('is_invoice_admin', models.BooleanField(default=False)),
                ('is_purchases_admin', models.BooleanField(default=False)),
                ('is_stock_admin', models.BooleanField(default=False)),
                ('is_user_admin', models.BooleanField(default=False)),
                ('is_accounts_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_delivery_pilot', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse_Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Item')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse_Transfer_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('is_recieved', models.BooleanField(default=False)),
                ('from_warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='BASE.Warehouse')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Item')),
                ('recieved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recieved_by', to=settings.AUTH_USER_MODEL)),
                ('to_warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='BASE.Warehouse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Item_Category'),
        ),
        migrations.AddField(
            model_name='branch_users',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Warehouse'),
        ),
        migrations.AddField(
            model_name='branch_stock',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BASE.Warehouse'),
        ),
    ]
