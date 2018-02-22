from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^$', views.tweetlist, name='list'),
	url(r'^(?P<id>[\w-]+)$', views.tweet_detail, name='detail'),
	url(r'^(?P<id>[\w-]+)/edit/$', views.tweet_update, name='update'),
	url(r'^(?P<id>[\w-]+)/delete/$', views.tweet_delete, name='delete'),
]
