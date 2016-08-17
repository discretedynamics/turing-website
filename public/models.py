from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Contributor(models.Model):
    name = models.CharField('Contributor Name', max_length=50)
    email = models.EmailField('Email', unique=True)
    personal_website = models.URLField('Personal Website', null=True, blank=True)
    organization = models.CharField('Organization', max_length=200)
    organization_website = models.URLField('Organization Website', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    name = models.CharField('Algorithm Name', max_length=200, default='NEW_ALGORITHM')
    versions = models.CharField('Algorithm Versions', max_length=200, default="['latest']")
    new_version = models.CharField('A new version', max_length=10, null=True, blank=True)
    summary = models.CharField('Summary', max_length=200, null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)
    website = models.URLField('Website', null=True, blank=True)
    docker_image = models.CharField('Docker Image', max_length=50)
    submit_date = models.DateTimeField('Date Submitted', default=timezone.now, blank=True)
    status = models.CharField('Algorithm Availability', max_length=20, default='pending')
    pub_date = models.DateTimeField('Date Published', blank=True, null=True)

    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name


class Workflow(models.Model):
    name = models.CharField('Workflow Name', max_length=200)
    description = models.CharField('Description', max_length=10000)
    workflow_json = models.TextField('Workflow JSON')
    screenshot_path = models.CharField('Screenshot Path', max_length=200, blank=True, null=True)
    file_path = models.CharField('File Path', max_length=200, blank=True, null=True)
    submit_date = models.DateTimeField('Date Submitted', default=timezone.now, blank=True)
    status = models.CharField('Workflow Availability', max_length=20, default='pending')
    pub_date = models.DateTimeField('Date Published', blank=True, null=True)

    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name