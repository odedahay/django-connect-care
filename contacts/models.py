from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    cv_file = models.FileField(upload_to='uploads/cvs/', null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name