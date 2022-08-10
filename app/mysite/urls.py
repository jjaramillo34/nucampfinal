"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib.sitemaps import views
from blog.sitemaps import PostSitemap
from courses.sitemaps import CoursesSitemap

sitemaps = {
    'blog': PostSitemap,
    'courses': CoursesSitemap,
}

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('portfolio/', include('projects.urls')),
    path('courses/', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('services/', include('services.urls')),
    path('resume/', include('resume.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('rosetta/', include('rosetta.urls')),  # NEW
    path('tinymce/', include('tinymce.urls')),
    #path('sitemap.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}}, name='django.contrib.sitemaps.views.sitemap'),
    
    path('sitemap.xml', views.index, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    
)