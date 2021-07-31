from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.DopeUsersListView.as_view(), name='users'),
    #url(r'^user/(?P<pk>\d+)$', views.DopeUserDetailView.as_view(), name='user'),
    url(r'^user/(?P<slug>[-\w]+)$', views.DopeUserDetailView.as_view(), name='user'),
    url(r'^user/(?P<slug>[-\w]+)/edit/$', views.EditDopeUserView.as_view(), name='edit'),

]

