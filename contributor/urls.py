from django.conf.urls import url

from . import views

app_name = 'contributor'

urlpatterns = [
    url(r'^profile/', views.profile, name='profile'),
    url(r'^update-profile/', views.update_profile, name='update-profile'),
    url(r'^algorithms/how-to/', views.algorithms_how_to, name='algorithms-how-to'),
    url(r'^algorithms/list/', views.my_algorithms, name='my-algorithms'),
    url(r'^algorithms/submit/', views.submit_algorithm, name='submit-algorithm'),
    url(r'^algorithms/submit-info/', views.submit_algorithm_info, name='submit-algorithm-info')
]