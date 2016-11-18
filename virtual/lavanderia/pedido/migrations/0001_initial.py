# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 19:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacao', '0004_cartao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField(auto_now=True)),
                ('data_busca', models.DateField(default=datetime.datetime.now)),
                ('data_entrega', models.DateField(null=True)),
                ('valor_pedido', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pecas_branca', models.BooleanField(default=False)),
                ('endereco_busca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_busca', to='autenticacao.Endereco')),
                ('endereco_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_entrega', to='autenticacao.Endereco')),
                ('pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_pagamento', to='autenticacao.Cartao')),
            ],
        ),
        migrations.CreateModel(
            name='TipoRoupa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, b'BANHO'), (2, b'CAMA'), (3, b'MESA'), (4, b'LUXO'), (99, b'OUTROS')], default=99)),
                ('quantidade', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipos_roupas', to='pedido.Pedido')),
            ],
        ),
    ]