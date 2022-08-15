from . import views
from django.urls import path

app_name = "courses"

urlpatterns = [
    path('', views.courses, name='courses'),
    path('courses/<int:pk>/', views.DetailView.as_view(), name='course_detail'),
]

