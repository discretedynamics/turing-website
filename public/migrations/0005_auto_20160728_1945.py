# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20160725_2052'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Contributor',
        ),
        migrations.AddField(
            model_name='algorithm',
            name='versions',
            field=models.CharField(default="['latest']", max_length=10, verbose_name='Algorithm Version'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Published'),
        ),
    ]
