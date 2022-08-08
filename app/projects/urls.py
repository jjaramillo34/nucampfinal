from . import views
from django.urls import path

app_name = "projects"

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    #path('porfolio/<slug:slug>/', views.project_detail, name='project_detail'),
]

