# Generated by Django 3.1.3 on 2020-11-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='sub_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
