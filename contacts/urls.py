from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.DopeUsersListView.as_view(), name='users'),
    url(r'^user/(?P<slug>[-\w]+)/$', views.DopeUserDetailView.as_view(), name='user'),
    url(r'^user/<slug>/edit/$', views.UpdateDopeUserView.as_view(), name='edit'),
    url(r'^user/<slug>/settings/$', views.SettingAccount.as_view(), name='settings'),
    url(r'^profile/$', views.profile, name='profile')

]

