# Generated by Django 5.0.1 on 2024-02-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_rename_name_setting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='blog_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
