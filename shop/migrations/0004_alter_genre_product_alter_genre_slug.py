# Generated by Django 4.2.5 on 2023-09-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='product_genre', to='shop.product'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
