from django.contrib import admin

from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['order_by', 'name', 'is_published']
    list_display_links = ('name',)
    list_editable = ('order_by','is_published',)

admin.site.register(Testimonial,TestimonialAdmin)

