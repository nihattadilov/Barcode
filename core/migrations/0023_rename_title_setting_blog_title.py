# Generated by Django 5.0.1 on 2024-02-26 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_rename_blog_title_setting_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='title',
            new_name='blog_title',
        ),
    ]
