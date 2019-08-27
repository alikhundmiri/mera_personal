from django.conf import settings
# from django.conf.urls import url, include
from django.urls import path, include

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView, RedirectView

from cv_db.views import (
		cv,
		resume,
	)

from .sitemapSettings import BlogSitemap, BlogTagsSitemap, WorkSitemap, WorkPublishedSitemap
from accounts.views import (login_view, logout_view, register_view)

sitemaps = {
    "blog" : BlogSitemap,
    "blogTag" : BlogTagsSitemap,
    "work" : WorkSitemap,
    "products" : WorkPublishedSitemap
}

# ''
urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', include('blogs.urls', namespace="blogs")),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('cv/', include('cv_db.urls', namespace="document")),

    path('resume/', RedirectView.as_view(url='https://personal-website-ali-1.s3.amazonaws.com/static/download/pdf/Ali_resume.pdf'), name='resume'),
    path('metro_project/', RedirectView.as_view(url='https://docs.google.com/spreadsheets/d/17GXgiQyL5MTAM05MA7Soi70530gheSJF_z_hWN2GNAk/edit?usp=sharing'), name='metro_project'),
    path('work/', include('first.urls', namespace="work")),

    path('links/', include('customredirect.urls', namespace="customredirect")),

    # Urls from Accounts. Login, Logout, Register
    path('ogin/',login_view, name='login' ),
    path('ogout/', logout_view, name='logout'),
    path('egister/', register_view, name='register'),


    path('base', TemplateView.as_view(template_name='base_jan_2018.html'), name='base18'),

    # index page.
    path('', TemplateView.as_view(template_name='landing_page.html'), name='home'),
    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
