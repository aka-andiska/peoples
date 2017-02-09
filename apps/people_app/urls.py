from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.destroy, name='delete'),
    url(r'^group/(?P<id>\d+)$', views.group, name='group'),
    url(r'^group_list$', views.group_list, name='group_list'),
    url(r'^group_create$', views.group_create, name='group_create'),
    url(r'^group_edit/(?P<id>\d+)$', views.group_edit, name='group_edit'),
    url(r'^group_delete/(?P<id>\d+)$', views.group_destroy, name='group_delete'),

    # url(r'^back/(?P<id>\d+)$', views.back, name='back'),

]