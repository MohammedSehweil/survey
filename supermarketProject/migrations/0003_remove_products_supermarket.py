# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarketProject', '0002_auto_20170403_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='supermarket',
        ),
    ]
