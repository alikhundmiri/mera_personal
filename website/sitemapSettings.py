from django.contrib.sitemaps import Sitemap

# Imports from all apps
from blogs.models import Post, taggers
from cereminder.models import events
from first.models import mywork, hosted_projects



############# C R A W L   T H E S E 
# Blog
# Cereminder
# Work First
# Poetist

############# D O N 'T   C R A W L    T H E S E
# CV
# Dinner


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Post.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.updated



class BlogTagsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return taggers.objects.all()



class CereminderSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return events.objects.all()



class WorkSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return mywork.objects.all()

    def lastmod(self, obj):
        return obj.updated



class WorkPublishedSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return hosted_projects.objects.all()

    def lastmod(self, obj):
        return obj.updated