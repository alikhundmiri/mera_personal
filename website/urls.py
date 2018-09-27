from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView, RedirectView

from cv_db.views import (
		cv,
		resume,
	)
import dinner

from .sitemapSettings import BlogSitemap, BlogTagsSitemap, CereminderSitemap, WorkSitemap, WorkPublishedSitemap
from accounts.views import (login_view, logout_view, register_view)

sitemaps = {
    "blog" : BlogSitemap,
    "blogTag" : BlogTagsSitemap,
    "cereminder" : CereminderSitemap,
    "work" : WorkSitemap,
    "products" : WorkPublishedSitemap
}

# ''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blogs.urls', namespace="blogs")),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^cv/', include('cv_db.urls', namespace="document")),
    url(r'^dinner/', include('dinner.urls', namespace="dinner")),
    url(r'^resume/$', RedirectView.as_view(url='https://personal-website-ali-1.s3.amazonaws.com/static/download/pdf/Ali_resume.pdf'), name='resume'),
    url(r'^metro_project/$', RedirectView.as_view(url='https://docs.google.com/spreadsheets/d/17GXgiQyL5MTAM05MA7Soi70530gheSJF_z_hWN2GNAk/edit?usp=sharing'), name='metro_project'),
    url(r'^work/', include('first.urls', namespace="work")),
    url(r'^tweetme/', include('tweetme.urls', namespace="tweetme")),
    url(r'^links/', include('customredirect.urls', namespace="customredirect")),

    # Urls from Accounts. Login, Logout, Register
    url(r'login/',login_view, name='login' ),
    url(r'logout/', logout_view, name='logout'),
    url(r'register/', register_view, name='register'),

    # Apps on Showcase
    url(r'^ceremony/', include('cereminder.urls', namespace="cereminder")),

    url(r'^base', TemplateView.as_view(template_name='base_jan_2018.html'), name='base18'),

    # index page.
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt', include('robots.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
