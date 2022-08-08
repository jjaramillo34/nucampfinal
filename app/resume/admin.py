from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.contrib.postgres import fields
from .models import Resume, Aside
from django_json_widget.widgets import JSONEditorWidget
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(Resume)
class ResumeAdmin(TranslatableAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

#admin.site.register(Resume, ResumeAdmin)
admin.site.register(Aside, TranslatableAdmin)
