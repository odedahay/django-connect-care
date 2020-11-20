from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):

    list_display =('id', 'name', 'email', 'phone', 'cv_file', 'contact_date', 'message')
    list_display_links = ('id', 'name', 'cv_file')
    search_fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)