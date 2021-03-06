# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BASE', '0002_remove_system_setting_pos_from_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_admin',
            name='is_branches_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_admin',
            name='is_manufacture_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_admin',
            name='is_reports_admin',
            field=models.BooleanField(default=False),
        ),
    ]
