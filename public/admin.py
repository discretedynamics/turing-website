from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Algorithm
from .models import Paper
from .models import Contributor

admin.site.register(Algorithm)
admin.site.register(Paper)
admin.site.register(Contributor)