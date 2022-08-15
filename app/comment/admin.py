from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Comment
from django.utils.translation import gettext_lazy as _

# Register your models here.
class CommentAdmin(TranslatableAdmin):
    list_display = ('post', 'name', 'active')
    fieldsets = (
        (None, {
            'fields': ('post', 'name', 'email', 'body', 'active'),
        }),
    )
    
    def title_column(self, object):
        return object.body
    title_column.short_description = _("Body")
    title_column.admin_order_field = "translations__body"

    def get_queryset(self, request):
        # Limit to a single language!
        language_code = self.get_queryset_language(request)
        return super(CommentAdmin, self).get_queryset(request).translated(language_code)
    
    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)

admin.site.register(Comment, CommentAdmin)