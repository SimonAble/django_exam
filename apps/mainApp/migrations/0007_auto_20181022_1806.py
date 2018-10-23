# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20181022_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='users',
        ),
        migrations.AddField(
            model_name='trip',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='mainApp.User'),
            preserve_default=False,
        ),
    ]
