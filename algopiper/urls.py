from django.conf.urls import url

from . import views

app_name = 'algopiper'

urlpatterns = [
    url(r'^api/v1/list/$', views.manager_list, name='manager-list'),
    url(r'^api/v1/deploy$', views.manager_deploy, name='manager-deploy'),
    url(r'^$', views.launch, name='launch'),
    url(r'^(?P<port_number>[0-9]+)$', views.view_algopiper_page, name='view-algopiper'),
    url(r'^run/(?P<workflow_id>[0-9]+)$', views.run_workflow, name='run-workflow')
]