from django.conf.urls import url

from . import views

app_name = 'contributor'

urlpatterns = [
    url(r'^profile/', views.profile, name='profile'),
]