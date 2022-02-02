from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.start, name='start'),
    url(r'^profiles/$', views.DopeUsersListView.as_view(), name='users'),
    url(r'^profile/(?P<slug>[-\w]+)/$', views.DopeUserDetailView.as_view(), name='user'),
    url(r'^profile/<slug>/edit/$', views.UpdateDopeUserView.as_view(), name='edit'),
    # url(r'^profile/<slug>/edit/$', views.update, name='edit'),
    url(r'^profile/<slug>/settings/$', views.SettingAccount.as_view(), name='settings'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^log/$', views.log),

]

