# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-19 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20160519_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='slice',
            name='description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Description of This Slice'),
        ),
    ]
