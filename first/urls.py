from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from .views import (
    first_list,
    first_detail,
    hosted_detail,
)

app_name = "first"

urlpatterns = [
    path('', first_list, name='list'),
    path('(<str:slug>/', first_detail, name='detail'),
    path('(<str:slug>/hosted', hosted_detail, name='hosted'),
]
