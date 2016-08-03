# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0012_delete_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='status',
            field=models.CharField(default='pending', max_length=10, verbose_name='Algorithm Availability'),
        ),
        migrations.AddField(
            model_name='algorithm',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Submitted'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='contributor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='public.Contributor'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Algorithm Name'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='summary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
    ]
