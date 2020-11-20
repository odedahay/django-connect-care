from django.contrib import admin

from .models import Program

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['order_by','level', 'title', 'slug', 'is_published']
    list_display_links = ('level', 'slug')
    list_editable = ('order_by', 'title','is_published',)

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Program, ProgramAdmin)