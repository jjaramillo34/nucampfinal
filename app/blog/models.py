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

class Post(TranslatableModel):
    cover = models.ImageField(upload_to='featured_images/%Y/%m/%d/')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    translations = TranslatedFields(
        title = models.CharField(_("Title"),max_length=200, unique=True),
        title_short = models.CharField(max_length=200),
        body = RichTextUploadingField(blank=True),
        #body = tinymce_models.HTMLField(blank=True),
        content = models.TextField(_("Content"), blank=True)
    )
    
    class Meta:
        ordering = ['-created_on', 'id']
        
    def __str__(self):
        return f"Title: {self.title}"
    
class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=150)
    name = models.CharField(max_length=100)
    
    
    