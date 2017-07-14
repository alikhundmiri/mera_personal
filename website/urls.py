from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from cv_db.views import (
		cv,
		resume,
	)
import dinner

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blogs.urls', namespace="blogs")),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^cv/', include('cv_db.urls', namespace="document")),
    url(r'^dinner/', include('dinner.urls', namespace="dinner")),
    url(r'^resume/$', RedirectView.as_view(url='https://personal-website-ali-1.s3.amazonaws.com/static/download/pdf/Ali_resume.pdf'), name='resume'),
    url(r'^work/', include('first.urls', namespace="work")),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
