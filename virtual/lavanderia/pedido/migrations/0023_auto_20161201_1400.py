# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 17:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0022_auto_20161201_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrega',
            field=models.DateField(default=datetime.datetime(2016, 12, 1, 14, 0, 54, 770546)),
        ),
    ]