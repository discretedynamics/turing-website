from django.conf.urls import url

from . import views

app_name = 'algopiper'

urlpatterns = [
    url(r'^$', views.launch, name='launch')
]