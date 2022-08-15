from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Contact(models.Model):
    CHOICES = (
        ('0', _("Select a service package you're interested in...")),
        ('1', _('Basic')),
        ('2', _('Standard')),
        ('3', _('Premium')),
        ('4', _('Not sure')),
    )
    question = models.CharField(max_length=1, choices=CHOICES)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.email
    