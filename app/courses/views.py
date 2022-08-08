from django.shortcuts import render
from courses.models import Course


# Create your views here.

def courses(request):
    courses = Course.objects.filter(status=1).order_by('-obtained_date')
    context = {'courses': courses}
    print(context)
    return render(
        request=request,
        template_name="home/courses.html",
        context=context
    )
