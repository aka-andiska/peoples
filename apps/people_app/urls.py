from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.destroy, name='delete'),
    url(r'^group/(?P<id>\d+)$', views.group_1, name='group_1'),
    url(r'^group/(?P<id>\d+)$', views.group_2, name='group_2'),
]