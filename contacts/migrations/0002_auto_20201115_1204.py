# Generated by Django 3.1.3 on 2020-11-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/cvs/'),
        ),
    ]
