from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^$', views.blog_list, name='list'),
	url(r'^tags/$', views.blog_all_tag, name='all_tag'),
	url(r'^archive/$', views.blog_archive, name='archive'),
	url(r'^create/$', views.blog_create, name='create'),
	url(r'^(?P<slug>[\w-]+)$', views.blog_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/edit/$', views.blog_update, name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', views.blog_delete, name='delete'),
	url(r'^tags/(?P<slug>[\w-]+)$', views.blog_tag, name='tag_list'),
]
