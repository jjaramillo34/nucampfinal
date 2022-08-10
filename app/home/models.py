from pyexpat import model
from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
# Create your models here.

STATUS = (
    (0, _(u"Draft")),
    (1, _(u"Publish"))
)

class Home(TranslatableModel):
    site = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    img_header = models.ImageField(upload_to='home')
    img_content = models.ImageField(upload_to='home')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    jobs = JSONField(null=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=60, unique=True),
        description_header = models.TextField(),
    )
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.site}"

    