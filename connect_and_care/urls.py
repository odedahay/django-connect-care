from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('programs/', include('programs.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('news/', include('news.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
