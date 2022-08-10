from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    #path('', views.ContactFormView.as_view() , name='contact'),
    path('', views.contact_view , name='contact'),
]