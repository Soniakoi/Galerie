# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-22 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phoros', '0006_auto_20190722_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]