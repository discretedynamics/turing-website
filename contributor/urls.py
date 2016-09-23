from django.conf.urls import url

from . import views

app_name = 'contributor'

urlpatterns = [
    url(r'^profile$', views.profile, name='profile'),
    url(r'^update-profile$', views.update_profile, name='update-profile'),
    url(r'^algorithms/how-to$', views.algorithms_how_to, name='algorithms-how-to'),
    url(r'^algorithms/list$', views.my_algorithms, name='my-algorithms'),
    url(r'^algorithms/submit$', views.submit_algorithm, name='submit-algorithm'),
    url(r'^algorithms/submit-info$', views.submit_algorithm_info, name='submit-algorithm-info'),
    url(r'^algorithms/delete-algorithm/(?P<algorithm_id>[0-9]+)$', views.delete_algorithm, name='delete-algorithm'),
    url(r'^algorithms/unpublish-algorithm/(?P<algorithm_id>[0-9]+)$', views.unpublish_algorithm, name='unpublish-algorithm'),
    url(r'^algorithms/submit-new-version/(?P<algorithm_id>[0-9]+)$', views.submit_new_version, name='submit-new-version'),
    url(r'^workflows/how-to$', views.workflows_how_to, name='workflows-how-to'),
    url(r'^workflows/list$', views.my_workflows, name='my-workflows'),
    url(r'^workflows/submit$', views.submit_workflow, name='submit-workflow'),
    url(r'^workflows/submit-info$', views.submit_workflow_json, name='submit-workflow-json'),
    url(r'^workflows/delete-workfow/(?P<workflow_id>[0-9]+)$', views.delete_workflow, name='delete-workflow'),
    url(r'^worfklows/unpublish-workflow/(?P<workflow_id>[0-9]+)$', views.unpublish_workflow, name='unpublish-workflow')
]