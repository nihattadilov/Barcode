# Generated by Django 5.0.1 on 2024-02-24 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_setting_facebook_alter_setting_instagram_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='name',
            new_name='title',
        ),
    ]
