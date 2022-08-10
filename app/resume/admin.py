from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.contrib.postgres import fields
from django.db.models import JSONField
from .models import Resume
from django_json_widget.widgets import JSONEditorWidget
from django.utils.translation import gettext_lazy as _

# Register your models here.

#@admin.register(Resume)
#class ResumeAdmin(TranslatableAdmin):
#    formfield_overrides = {
#        JSONField: {'widget': JSONEditorWidget},
#    }

admin.site.register(Resume, TranslatableAdmin)

