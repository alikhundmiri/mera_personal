from django.conf.urls import url, include
from .views import (
    cv,
    resume,
)

app_name = "cv_db"

urlpatterns = [
    url(r'^$', cv, name='cv'),
    url(r'^resume/', resume, name='resume'),
]
