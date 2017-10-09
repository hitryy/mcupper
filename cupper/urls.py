from django.conf.urls import url, include

from cupper import views

app_name = 'cupper'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$', views.do_login, name='login'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'logged_out/$', views.logged_out, name='logged_out'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'signup_success/$', views.signup_success, name='signup_success'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'activation_success/$', views.activation_success)

]