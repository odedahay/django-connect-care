from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', ]
    list_display_links = ('title', 'slug')

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)
