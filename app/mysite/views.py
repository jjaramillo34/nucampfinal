from django.shortcuts import render

def page_not_found_view(request, exception):
    context = {}
    return render(request, 'home/404.html', context=context)

def page_forbidden(request, exception):
    context = {}
    return render(request, 'home/403.html', context=context)

def page_internal_error(request):
    context = {}
    return render(request, 'home/500.html', context=context)

def page_bad_request(request, exception):
    context = {}
    return render(request, 'home/400.html', context=context)