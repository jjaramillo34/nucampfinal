from django.shortcuts import render
from home.models import Home
from projects.models import Project
from courses.models import Course
from blog.models import Post
from services.models import Services
from testimonials.models import Testimonials

# Create your views here.

def home(request):
    homepage = Home.objects.filter(status=1).order_by('id')
    posts = Post.objects.filter(status=1).order_by('id')[:3]
    testimonials = Testimonials.objects.filter(active=True).order_by('id')
    projects = Project.objects.filter(status=1).order_by('?')[:4]
    courses = Course.objects.filter(status=1).order_by('-obtained_date')[:6]
    services = Services.objects.filter(status=1).order_by('id')[:8]
    context = {
        'homepage': homepage,
        "testimonials": testimonials, 
        'projects': projects, 
        'courses': courses, 
        'posts': posts, 
        'services': services}
    print(context)
    return render(
        request=request,
        template_name="home/index.html",
        context=context
    )