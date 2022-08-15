from . import views
from django.urls import path
#from django.conf.urls import url

app_name = "services"
urlpatterns = [
    path('', views.services, name='services'),
]