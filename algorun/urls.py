from django.conf.urls import url

from . import views

app_name = 'algorun'

urlpatterns = [
    url(r'^$', views.launch, name='launch')
]