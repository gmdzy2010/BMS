# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='Barcode名')),
                ('sequence', models.CharField(max_length=20, verbose_name='序列')),
            ],
            options={
                'verbose_name_plural': 'Barcode管理',
                'verbose_name': 'Barcode管理',
            },
        ),
        migrations.CreateModel(
            name='Primer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='引物名称')),
                ('sequence', models.CharField(max_length=50, verbose_name='序列')),
            ],
            options={
                'verbose_name_plural': '引物管理',
                'verbose_name': '引物管理',
            },
        ),
    ]
