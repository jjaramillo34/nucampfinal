from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Services
from django.utils.translation import gettext_lazy as _

# Register your models here.
admin.site.register(Services, TranslatableAdmin)
