from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

class Program(models.Model):
    order_by = models.IntegerField(unique=True, blank=True, null=True)
    level = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    hour = models.CharField(max_length=100)
    #content = RichTextField()
    content = RichTextUploadingField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering =('order_by',)
        verbose_name = 'program'
        verbose_name_plural = 'programs'

    def __str__(self):
        return self.title