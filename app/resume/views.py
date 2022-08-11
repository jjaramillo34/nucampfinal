import json
from django.shortcuts import render
from home.models import Home
from resume.models import Resume

# Create your views here.

def resume_view(request):
    homepage = Home.objects.filter(status=1).order_by('id')
    resume = Resume.objects.filter(status=1).order_by('id')

    context = {'homepage': homepage, 'resume': resume}
    
    return render(
        request=request,
        template_name="home/resume.html",
        context=context
    )
