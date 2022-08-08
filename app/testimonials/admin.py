from django.contrib import admin
from parler.admin import TranslatableAdmin
from testimonials.models import Testimonials

# Register your models here.
admin.site.register(Testimonials, TranslatableAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'title')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
