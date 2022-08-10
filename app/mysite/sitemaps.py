from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return ['home:home', 'blog:blog', 'courses:courses', 'projects:portfolio', 'resume:resume', 'services:services']

    def location(self, item):
        return reverse(item)