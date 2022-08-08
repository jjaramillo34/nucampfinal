from gettext import translation
from django.db import models
from django.contrib.postgres.fields import ArrayField
#from django.contrib.postgres.fields import JSONField
from picklefield.fields import PickledObjectField
from django.db.models import JSONField
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields
from tinymce import models as tinymce_models
from django.utils.translation import gettext_lazy as _
# Create your models here.

STATUS = (
    (0, _(u"Draft")),
    (1, _(u"Publish"))
)

class Resume(TranslatableModel):
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    translations = TranslatedFields(
        job_title = models.CharField(_("Title"),max_length=50, unique=True),
        jobs = JSONField(null=True),
        skills = JSONField(null=True),
        education = JSONField(null=True),
        awards = JSONField(null=True),
        languagues = JSONField(null=True),
        interests = JSONField(null=True),
    )
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return f"Title: {self.job_title}"
    
class Aside(TranslatableModel):
    title = models.CharField(max_length=50, null=True)
    #description = models.TextField(null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    translations = TranslatedFields(
        description = models.TextField(null=True)
    )
