from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.db.models import JSONField
from .models import Home
from django_json_widget.widgets import JSONEditorWidget
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(Home)
class HomeAdmin(TranslatableAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

#class HomeAdmin(TranslatableAdmin):
#    #prepopulated_fields = {"slug": ("translations__title",)}
#    list_display = ('title', 'status', 'site')
#    fieldsets = (
#        (None, {
#            'fields': ('title', 'name', 'img_header', 'img_content', 'jobs', 'description_header', 'status'),
#        }),
#    )


#admin.site.register(Home, HomeAdmin)