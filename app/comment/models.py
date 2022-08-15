from django.db import models
from blog.models import Post
from parler.models import TranslatableModel, TranslatedFields, TranslatedField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Comment(TranslatableModel):
    
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments', null=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    
    translations = TranslatedFields(
        body = models.TextField()
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.post}"
    