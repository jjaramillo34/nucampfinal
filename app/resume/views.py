import json
from django.shortcuts import render
from django.views.generic import DetailView
from resume.models import Aside
from resume.models import Resume

# Create your views here.

def resume_view(request):
    resume = Resume.objects.filter(status=1).order_by('id')
    aside = Aside.objects.filter(status=1).order_by('id')
    
    d2 = [
        {'id': 1, 'title': 'Technical', 'items':[{'item': 'JavaScript/Angular/React/Vue'}]},
        {'id': 2, 'title': 'Profesional', 'items':[{'item': 'Effective communication'}]},
    ]
    
    di1 = [
        {'id':1,'title': 'AI Model Data Specialist', 'time':'Agilent | Oct 2020 - Apr 2022', 'company': 'Agilent Technologies – Leading analytical instrumentation development and manufacturing company' , 'items': [
            {'item': 'Tag activities in customer data to create and provide models for each new customer for the AI Analyst to enhance AI training through regression models, helping evaluate changes in equipment performance'},
            {'item': 'Developed the “Golden Tag Set” to determine a standard range for product test specifications to apply to future assets, minimizing the need for additional research and saving about ~2 weeks of analysis time'},
            {'item': '•	Updated Excel templates using VBA and Python scripts to automate dashboards and seamlessly compare old and new data, slashing time spent on equipment research by ~2 hours per week'},
            {'item': 'Tag activities in customer data to develop a model for each new customer asset and provide these to the AI Analyst for AI training'},
            {'item': 'Engage with users and review instrument log files to understand utilization and deploy asset monitors to model the tagging process and optimize AI for connected assets'},
            {'item': 'Review and approve model predictions with the AI Model Team as Tier 2 support before releasing models to customers'},
            {'item': 'Parse data faster using Python scripts and develop scrapers to read XML files and locate data for clients, conducting proactive model maintenance and scheduled re-trainability'},
        ]},
        {'id':1,'title': 'Junior Data Engineer', 'time':'CareerMD | Jun 2019 - Nov 2019', 'company': 'Careermd.com - Healthcare and medical recruitment website' , 'items': [
            {'item': 'Gathered and processed ~6K raw data points of medical professionals at scale (including writing scripts, web scraping, calling APIs, PDF, image parsing, and writing applications) and deployed SQL to compare data and upload it into PostgreSQL & AWS'},
            {'item': 'Built custom Python scripts using Beautiful Soup, Selenium, Requests, and other Python libraries as per data requirements to automate data parsing and extraction, saving ~3 weeks'},
            {'item': 'Collaborated with Project Management to provide timely estimates, updates & status for data collection, completing the project 6 months early and helping attract 400% more interest at recruiting events'},
            {'item': 'Performed data reconciliation procedures to confirm the completeness of data extraction and wrote ~300 Python scripts to train NLP using machine learning algorithms for pattern recognition, improving reusability'},
            {'item': '•	Partnered with senior data engineer to support feature engineering, model training frameworks, & model deployments at scale'},    
        ]},
        ]
    
    di1 = json.dumps(di1)
    loaded = json.loads(di1)
    
    print(loaded)
    
    context = {'resume': resume}
    #print(context)
            #print(i['item'])
    
    return render(
            request=request,
            template_name="home/resume.html",
            context=context
    )

class TinyMceDetail(DetailView):
    model = Resume
    template_name  = 'home/resume.html'