# Generated by Django 2.2.28 on 2024-02-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=' '),
            preserve_default=False,
        ),
    ]
