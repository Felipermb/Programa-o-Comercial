# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_pedido_nome_responsavel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='pecas_branca',
        ),
        migrations.AddField(
            model_name='tiporoupa',
            name='pecas_branca',
            field=models.BooleanField(default=False),
        ),
    ]
