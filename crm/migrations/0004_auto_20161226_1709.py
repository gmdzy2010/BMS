# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-26 09:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20161222_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='linker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='联络人'),
        ),
    ]
