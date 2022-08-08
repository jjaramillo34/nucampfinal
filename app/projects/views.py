from django.shortcuts import render
from projects.models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.filter(status=1).order_by('id')
    context = {'projects': projects}
    print(context)
    return render(
        request=request,
        template_name="home/portfolio.html",
        context=context
    )
