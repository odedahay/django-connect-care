from django.db import models
from ckeditor.fields import RichTextField

class Testimonial(models.Model):
    order_by = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    #content = RichTextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering =('is_published',)
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'

    def __str__(self):
        return self.name

