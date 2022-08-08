from . import views
from django.urls import path

app_name = "courses"

urlpatterns = [
    path('', views.courses, name='courses'),
]

