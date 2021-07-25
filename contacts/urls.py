from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.DopeUsersListView.as_view(), name='users'),
    # r'^book/(?P<stub>[-\w]+)$'
    url(r'^user/(?P<pk>\d+)$', views.DopeUserDetailView.as_view(), name='user'),

]

