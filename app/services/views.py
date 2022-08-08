from django.shortcuts import render

# Create your views here.
def services(request):
    context = {}
    return render(
        request=request,
        context=context,
        template_name="home/services.html",
    )
