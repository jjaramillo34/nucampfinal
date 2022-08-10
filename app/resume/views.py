import json
from django.shortcuts import render
from resume.models import Resume

# Create your views here.

def resume_view(request):
    resume = Resume.objects.filter(status=1).order_by('id')
    
    context = {'resume': resume}
    #print(context)
            #print(i['item'])
    
    return render(
            request=request,
            template_name="home/resume.html",
            context=context
    )
