from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Algorithm(models.Model):
    name = models.CharField('Algorithm Name', max_length=200)
    summary = models.CharField('Summary', max_length=200)
    description = models.TextField('Description')
    website = models.URLField('Website')
    docker_image = models.CharField('Docker Image', max_length=50)
    pub_date = models.DateTimeField('Date Published')

class Paper(models.Model):
    title = models.CharField('Paper Title', max_length=200)
    url = models.URLField('Link')

class Author(models.Model):
    name = models.CharField('Author Name', max_length=50)
    email = models.EmailField('Email')
    personal_website = models.URLField('Personal Website')
    organization = models.CharField('Organization', max_length=200)
    organization_website = models.URLField('Organization Website')
    join_date = models.DateTimeField(auto_now_add=True, blank=True)