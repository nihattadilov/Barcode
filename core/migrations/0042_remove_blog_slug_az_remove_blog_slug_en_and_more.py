# Generated by Django 4.2.10 on 2024-10-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_setting_background_photo1_setting_background_photo2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug_az',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug_tr',
        ),
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_tr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
