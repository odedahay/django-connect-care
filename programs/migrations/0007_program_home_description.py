# Generated by Django 3.1.3 on 2020-12-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0006_program_content_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='home_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
