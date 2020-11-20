from django.contrib import admin


from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','is_published',)
    list_display_links = ('title',)
    list_editable = ('slug','is_published',)

    prepopulated_fields = {'slug': ('title',)}

    search_fields = ('title',)
    list_per_page = 25

admin.site.register(News, NewsAdmin)