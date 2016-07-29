from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

DEFAULT_CONTRIBUTOR_ID=1


class Contributor(models.Model):
    name = models.CharField('Contributor Name', max_length=50)
    email = models.EmailField('Email')
    personal_website = models.URLField('Personal Website')
    organization = models.CharField('Organization', max_length=200)
    organization_website = models.URLField('Organization Website')
    join_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    name = models.CharField('Algorithm Name', max_length=200)
    versions = models.CharField('Algorithm Versions', max_length=10, default="['latest']")
    summary = models.CharField('Summary', max_length=200)
    description = models.TextField('Description')
    website = models.URLField('Website')
    docker_image = models.CharField('Docker Image', max_length=50)
    pub_date = models.DateTimeField('Date Published', auto_now_add=True, blank=True)

    admin_contributor = Contributor()
    admin_contributor.name = "Abdelrahman Hosny"
    admin_contributor.email = "aibrahim@uchc.edu"
    admin_contributor.personal_website = "http://www.abdelrahmanhosny.me"
    admin_contributor.organization = "Center for Quantitative Medicine, UConn Health"
    admin_contributor.organization_website = "http://cqm.uchc.edu"
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, default=DEFAULT_CONTRIBUTOR_ID)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name


class Paper(models.Model):
    title = models.CharField('Paper Title', max_length=200)
    url = models.URLField('Link')

    def __str__(self):
        return self.title


