from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='list'),
	url(r'^upcoming$', views.whatsnext, name='whatsnext'),
	url(r'^(?P<id>\d+)$', views.detail, name='detail'),
]
