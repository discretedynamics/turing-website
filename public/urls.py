from django.conf.urls import url

from . import views

app_name = 'public'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^algorithms$', views.algorithms, name='algorithms'),
    url(r'^algorithm/(?P<algorithm_id>[0-9]+)$', views.useAlgorithm, name='use_algorithm'),
    url(r'^workflows$', views.workflows, name='workflows'),
    url(r'^contribute$', views.contribute, name='contribute'),
    url(r'^about$', views.about, name='about'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^sign-up$', views.signup, name='sign-up'),
    url(r'^sign-up-submit$', views.signup_submit, name='sign-up-submit'),
    url(r'^sign-in$', views.signin, name='sign-in'),
    url(r'^sign-in-submit$', views.signin_submit, name='sign-in-submit'),
    url(r'^sign-out$', views.sign_out, name='sign-out')
]