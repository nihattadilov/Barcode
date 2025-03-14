# Generated by Django 4.2.10 on 2024-05-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='saqol', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug_az',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug_en',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug_tr',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
