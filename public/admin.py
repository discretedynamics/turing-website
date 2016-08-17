from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Algorithm
from .models import Contributor
from .models import Workflow

admin.site.register(Algorithm)
admin.site.register(Contributor)
admin.site.register(Workflow)