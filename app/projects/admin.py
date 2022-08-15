from django.contrib import admin
from parler.admin import TranslatableAdmin
from projects.models import Project

# Register your models here.
admin.site.register(Project, TranslatableAdmin)