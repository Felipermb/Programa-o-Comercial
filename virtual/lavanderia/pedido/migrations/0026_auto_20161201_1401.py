# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 17:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0025_auto_20161201_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrega',
            field=models.DateField(default=datetime.datetime(2016, 12, 3, 14, 1, 36, 957360)),
        ),
    ]
