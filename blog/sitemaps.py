from django.contrib.sitemaps import Sitemap
from .models import Post, Project
from django.urls import reverse
from blog.urls import urlpatterns as homeUrls

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.post_date

    def location(self,obj):
        return "/" + obj.post_slug

class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def lastmod(self,obj):
        return obj.project_date

    def location(self, obj):
        return "/projects/" + obj.project_slug

class StaticViewSiteMap(Sitemap):
    priority = 0.4
    changefreq = 'weekly'

    def items(self):
        myList = []
        for url in homeUrls:
            if url.name != 'oneproject' and url.name != 'post' and url.name != 'index':
                myList.append('blog:'+ url.name)
        return myList

    def location(self,item):
        return reverse(item)

class SpecialViewSiteMap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        myList = []
        for url in homeUrls:
            if url.name == 'index':
                myList.append('blog:'+ url.name)
        return myList

    def location(self,item):
        return reverse(item)
