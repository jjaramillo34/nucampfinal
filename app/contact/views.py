import requests
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views import generic

from home.views import Home
from .decorators import check_recaptcha

from contact.forms import ContactForm

# Create your views here.

@check_recaptcha
class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = 'home/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recaptcha_key'] = settings.RECAPTCHA_PUBLIC_KEY
        print(f"My Recaptcha Key: {context['recaptcha_key']}")
        return context
    
    def get_success_url(self) -> str:
        print(f"Success URL: {self.request.path}")
        return self.request.path
    
    def form_valid(self, form):
        for field in form:
            print("Field Error:", field.name,  field.errors)
        print(form.is_valid())
        
        # retrieve token
        token = self.request.POST('g-recaptcha-response')
        if token:
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': token
            }
            # verify response with Google
            response = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data = data
            )
            result = response.json()
            # check results
            if result['success'] == True and result['score'] >= 0.5:
                form.save()
                email_subject = f'New contact {form.cleaned_data["name"]}: {form.cleaned_data["email"]}'
                email_message = f'''
                Name: {form.cleaned_data["name"]}
                Subject: {form.cleaned_data["question"]}
                Message: {form.cleaned_data["message"]}
                Email: {form.cleaned_data["email"]}
                '''
                send_mail(
                    email_subject,
                    email_message,
                    'contactme@datanaly.st',
                    ['contact@datanaly.st'],
                    fail_silently=False,
                )
                messages.add_message(self.request, messages.INFO, _('You Message Has Been Send Successfully'))
            #return super().form_valid(form)
            return render(self.request, 'home/contact.html', {
            'form': self.get_form(),
            'message': 'Thank you'
        })
    
    def form_invalid(self, form):
        form.add_error(None, _('Oops... something went wrong with the form'))
        for field in form:
            print("Field Error:", field.name,  field.errors)
        #print(form.form_invalid())
        return super().form_invalid(form)

@check_recaptcha    
def contact_view(request):
    homepage = Home.objects.filter(status=1).order_by('id')
    print(request.method)
    if request.method == "POST":
        form = ContactForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        print(form.is_valid())
        #print(form)u
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            email_subject = f'New contact {form.cleaned_data["name"]}: {form.cleaned_data["email"]}'
            email_message = f'''
            Name: {form.cleaned_data["name"]}
            Subject: {form.cleaned_data["question"]}
            Message: {form.cleaned_data["message"]}
            Email: {form.cleaned_data["email"]}
            '''
            send_mail(
                email_subject,
                email_message,
                'contactme@datanaly.st',
                ['contact@datanaly.st'],
                fail_silently=False,
            )
            #messages.success(request, 'New comment added with success!')
            messages.add_message(request, messages.INFO, _('You Message Has Been Send Successfully'))
            return redirect('contact:contact')
            #return render(request, 'home/success.html')
    else:
        form = ContactForm()
        print(form.is_valid())
        context = {'form': form, 'homepage': homepage}
        return render(request=request, template_name='home/contact.html', context=context)

