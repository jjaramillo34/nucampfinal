from . import views
from django.urls import path
from blog.models import Post

app_name = "blog"

urlpatterns = [
    path('', views.PostList, name='blog'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('validate/', views.validate_email, name='validate_email'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]