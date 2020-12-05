from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering =('title',)
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.title
