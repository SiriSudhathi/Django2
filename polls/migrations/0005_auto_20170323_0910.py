# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170323_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='address',
            field=models.TextField(max_length=30),
        ),
    ]