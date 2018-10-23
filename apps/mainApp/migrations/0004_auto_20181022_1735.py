# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20181022_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joined',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='joined',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='added_by',
        ),
        migrations.AddField(
            model_name='trip',
            name='users',
            field=models.ManyToManyField(related_name='users', to='mainApp.User'),
        ),
        migrations.DeleteModel(
            name='Joined',
        ),
    ]