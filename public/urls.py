from django.conf.urls import url

from . import views

app_name = 'public'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^algorithms/', views.algorithms, name='algorithms'),
    url(r'^workflows/', views.workflows, name='workflows'),
    url(r'^contribute/', views.contribute, name='contribute'),
    url(r'^about/', views.about, name='about')
]