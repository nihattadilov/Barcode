# Generated by Django 5.0.1 on 2024-02-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'ContactMail',
                'verbose_name_plural': 'ContactMails',
            },
        ),
    ]
