# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='year',
        ),
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
