from django.contrib import sitemaps
from django.urls import reverse

from courses.models import Course

class CoursesSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.9
    
    def items(self):
        return Course.objects.all()
    
    def lastmod(self, obj):
        return obj.created_on