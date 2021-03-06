# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_auto_20160728_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='versions',
            field=models.CharField(default="['latest']", max_length=10, verbose_name='Algorithm Versions'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='organization_website',
            field=models.URLField(default=None, verbose_name='Organization Website'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='personal_website',
            field=models.URLField(default=None, verbose_name='Personal Website'),
        ),
    ]
