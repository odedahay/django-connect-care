# Generated by Django 3.1.3 on 2020-11-26 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_auto_20201117_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='designation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]