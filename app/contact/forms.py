from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Contact

from captcha.fields import ReCaptchaField

from captcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox, ReCaptchaV3

CHOICES = (
        ('0', _("Select a service package you're interested in...")),
        ('1', 'Basic'),
        ('2', 'Standard'),
        ('3', 'Premium'),
        ('4', 'Not sure'),
    )

class ContactForm(forms.ModelForm):
    
    #captcha = ReCaptchaField()
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _(u'Name'), 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': _(u'Email'), 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': _(u'Enter your message'), 'class': 'form-control', 'cols': 100}),
            'question': forms.Select(choices=CHOICES, attrs={'class': 'form-select'}),
        }
        
    #def clean_name(self):
        #n = self.cleaned_data['name']
        #if len(n) < 2:
            #raise forms.ValidationError(_("Name must be at least 2 characters!")) 

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['question'].initial = '0'
    
    