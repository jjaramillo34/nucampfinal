from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
# Create your models here.

STATUS = (
    (0, _(u"Draft")),
    (1, _(u"Publish"))
)

class Course(TranslatableModel):
    platform = models.CharField(max_length=100, blank=True, null=True)
    categories = models.CharField(max_length=400, blank=True, null=True)
    cover = models.ImageField(upload_to='courses')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    obtained_date = models.DateTimeField()
    link = models.CharField(max_length=500, blank=True, null=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=200, unique=True),
        description = models.TextField(),
    )
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | {self.platform}"
