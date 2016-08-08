from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class RunningContainer(models.Model):
    visitor_id = models.CharField('Visitor ID', max_length=200)
    docker_image = models.CharField('Docker Image', max_length=200)
    container_id = models.CharField('Container ID', max_length=200)
    port_number = models.IntegerField('Port Number')
    started_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.container_id

    def time_to_delete(self):
        elapsed_time = timezone.now() - self.started_at
        if elapsed_time.hour > 12:
            return True
        else:
            return False
