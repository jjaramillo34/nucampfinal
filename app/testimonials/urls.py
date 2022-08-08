from django.urls import path

# importing views from views..py
from .views import TestiomonialsListView
urlpatterns = [
    path('', TestiomonialsListView.as_view()),
]