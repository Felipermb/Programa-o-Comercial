# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0008_auto_20161201_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartao',
            name='cliente',
            field=models.ForeignKey(default='User.id', on_delete=django.db.models.deletion.CASCADE, related_name='cartoes', to='autenticacao.Cliente'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(default='User.id', on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='autenticacao.Cliente'),
        ),
    ]
