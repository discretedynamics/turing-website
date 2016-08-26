from django.conf.urls import url

from . import views

app_name = 'algorun'

urlpatterns = [
    url(r'^$', views.launch, name='launch'),
    url(r'^view/(?P<port_number>[0-9]+)$', views.view_algorithm_page, name='view-algorithm')
]