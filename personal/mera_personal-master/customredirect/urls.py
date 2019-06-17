from django.conf.urls import url, include
from django.contrib import admin

from .views import (
	redirect_intro,
	redirect_link,
	redirect_new
)

app_name = "customredirect"

urlpatterns = [
    url(r'^$', redirect_intro, name='redirect_intro'),
    url(r'^new/$', redirect_new, name='redirect_new'),
    url(r'^(?P<slug>[\w-]+)/$', redirect_link, name='redirect_link'),

    # url for new link
    # url for redirect
]
