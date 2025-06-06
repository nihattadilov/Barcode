# Generated by Django 5.0.1 on 2024-04-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_blog_description2'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='media/about/')),
                ('image2', models.ImageField(upload_to='media/about/')),
                ('name', models.CharField(max_length=50)),
                ('name2', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('description2', models.TextField()),
                ('description3', models.TextField()),
                ('description4', models.TextField()),
                ('aforithm', models.TextField()),
                ('author', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
