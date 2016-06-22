from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^algorithms/', views.algorithms, name='workflows'),
    url(r'^workflows/', views.workflows, name='workflows'),
    url(r'^author/', views.author, name='author')
]