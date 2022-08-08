from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from tinymce import models as tinymce_models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
# Create your models here.

STATUS = (
    (0, _(u"Draft")),
    (1, _(u"Publish"))
)

class Services(TranslatableModel):
    icon = models.TextField(null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    translations = TranslatedFields(
        title = models.CharField(_("Title"),max_length=200, unique=True),
        content = models.TextField(_("Content"), blank=True)
    )
    
    class Meta:
        ordering = ['-created_on', 'id']
        
    def __str__(self):
        return f"Title: {self.title}"
    
    
    