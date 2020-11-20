from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=200,  unique=True, null=True)
    content = RichTextUploadingField(blank=True,null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering =('-pub_date',)
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title