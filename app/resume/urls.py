from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [
    #path('', views.ContactFormView.as_view() , name='contact'),
    #path('', views.TinyMceDetail.as_view() , name='resume'),
    path('', views.resume_view , name='resume'),
]