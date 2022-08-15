from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

# Create your models here.
STATUS = (
    (0, _("Draft")),
    (1, _("Publish"))
)

class Project(TranslatableModel):
    categories = models.CharField(max_length=400)
    cover = models.ImageField(upload_to='projects')
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=200, unique=True),
        description = models.TextField(),
        body = RichTextUploadingField(blank=True),
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
