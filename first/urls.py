from django.conf.urls import url, include
from django.contrib import admin

from .views import (
    first_list,
    first_detail,
    hosted_detail,
)

urlpatterns = [
    url(r'^$', first_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', first_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/hosted$', hosted_detail, name='hosted'),
]
