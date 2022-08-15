from django.contrib import admin
from parler.admin import TranslatableAdmin, SortedRelatedFieldListFilter
from courses.models import Course
from django.utils.translation import gettext_lazy as _

# Register your models here.
class CourseAdmin(TranslatableAdmin):
    list_display = ('title', 'platform','status')
    fieldsets = (
        (None, {
            'fields': ('title','platform', 'status', 'cover', 'description', 'obtained_date', 'categories'),
        }),
    )
    
    def title_column(self, object):
        return object.title
    title_column.short_description = _("Title")
    title_column.admin_order_field = "translations__title"

    def get_queryset(self, request):
        # Limit to a single language!
        language_code = self.get_queryset_language(request)
        return super(CourseAdmin, self).get_queryset(request).translated(language_code)
    
admin.site.register(Course, CourseAdmin)

