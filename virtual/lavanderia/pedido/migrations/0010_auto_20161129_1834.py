# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 21:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0009_auto_20161129_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrega',
            field=models.DateField(default=datetime.datetime(2016, 12, 1, 18, 34, 34, 64595)),
        ),
    ]