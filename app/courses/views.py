from django.shortcuts import render
from django.views.generic import DetailView
from courses.models import Course
from home.models import Home

# Create your views here.

def courses(request):
    homepage = Home.objects.filter(status=1)
    courses = Course.objects.filter(status=1).order_by('-obtained_date')
    context = {
        'homepage': homepage,
        'courses': courses
        }
    print(context)
    return render(
        request=request,
        template_name="home/courses.html",
        context=context
    )

class CourseDetailView(DetailView):
    model = Course
    template_name = 'recipe_detail.html'    