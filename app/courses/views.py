from django.shortcuts import render
from django.views.generic import DetailView
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

class RecipeDetailView(DetailView):
    model = Course
    template_name = 'recipe_detail.html'    