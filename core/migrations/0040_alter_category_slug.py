# Generated by Django 4.2.10 on 2024-05-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=' ', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
