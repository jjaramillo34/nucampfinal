from django.shortcuts import render
from django.http import HttpResponseNotFound
from sentry_sdk import capture_message

def page_not_found_view(request, exception):
    context = {}
    capture_message("Page not found!", level="error")

    return render(request, 'home/404.html', context=context)

def page_forbidden(request, exception):
    context = {}
    return render(request, 'home/403.html', context=context)

def page_internal_error(request):
    context = {}
    capture_message("Page not found!", level="error")
    #return HttpResponseNotFound("Not found")
    return render(request, 'home/500.html', context=context)

def page_bad_request(request, exception):
    context = {}
    return render(request, 'home/400.html', context=context)