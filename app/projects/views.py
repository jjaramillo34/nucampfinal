from django.shortcuts import render
from home.models import Home
from projects.models import Project

# Create your views here.

def portfolio(request):
    homepage = Home.objects.filter(status=1).order_by('id')
    projects = Project.objects.filter(status=1).order_by('id')
    context = {'projects': projects, 'homepage': homepage}
    print(context)
    return render(
        request=request,
        template_name="home/portfolio.html",
        context=context
    )
