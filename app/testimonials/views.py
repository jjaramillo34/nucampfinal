from django.shortcuts import render
from django.views.generic.list import ListView
from testimonials.models import Testimonials

# Create your views here.
class TestiomonialsListView(ListView):
    model = Testimonials
    
    def get_queryset(self, *args, **kwargs):
        qs = super(Testimonials, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs