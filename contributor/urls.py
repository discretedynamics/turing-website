from django.conf.urls import url

from . import views

app_name = 'contributor'

urlpatterns = [
    url(r'^profile/', views.profile, name='profile'),
    url(r'^update-profile/', views.update_profile, name='update-profile')
]