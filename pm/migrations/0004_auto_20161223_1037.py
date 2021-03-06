# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-23 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0003_sample_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='status',
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('NST', '未启动'), ('SSB', '样品提交'), ('QC', '质控完成'), ('LIB', '建库完成'), ('SEQ', '测序完成'), ('FIN', '完成'), ('PAU', '暂停')], default='NST', max_length=3, verbose_name='状态'),
        ),
    ]
