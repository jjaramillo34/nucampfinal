from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post, SubscribedUsers
from django.utils.translation import gettext_lazy as _

class PostAdmin(TranslatableAdmin):
    #prepopulated_fields = {"slug": ("translations__title",)}
    list_display = ('title', 'status', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'cover', 'status', 'author',  'content', 'body'),
        }),
    )
    
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }
    
    def title_column(self, object):
        return object.title
    title_column.short_description = _("Title")
    title_column.admin_order_field = "translations__title"

    def get_queryset(self, request):
        # Limit to a single language!
        language_code = self.get_queryset_language(request)
        return super(PostAdmin, self).get_queryset(request).translated(language_code)
    
    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)
        
#@admin.register(Post)
#class PostAdminTiny(TranslatableAdmin):
#    class Media:
#        pass
#        #js = ('assets/js/tinyInject.js',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(SubscribedUsers)