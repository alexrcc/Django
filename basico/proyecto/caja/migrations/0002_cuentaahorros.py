# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaAhorros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCuenta', models.CharField(max_length=15)),
                ('estado', models.BooleanField()),
                ('fechaApertura', models.DateTimeField(auto_now=True)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('idC', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='caja.Cliente')),
            ],
        ),
    ]
