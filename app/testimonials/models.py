from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Testimonials(TranslatableModel):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='testimonials')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    translations = TranslatedFields(
        description = models.TextField(),
        title = models.CharField(max_length=250)
    )
    
    def __str__(self) -> str:
        return self.title


