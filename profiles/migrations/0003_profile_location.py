# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Location', max_length=120),
        ),
    ]
