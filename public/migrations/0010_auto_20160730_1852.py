# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0009_auto_20160729_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]