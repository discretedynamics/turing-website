from django.conf.urls import url

from . import views

app_name = 'adam'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^algorithms/', views.algorithms, name='workflows'),
    url(r'^workflows/', views.workflows, name='workflows'),
    url(r'^author/', views.author, name='author')
]