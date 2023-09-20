from os.path import splitext
from PIL import Image

from django.db import models
from django.urls import reverse

RUS_LANGUAGE = (
    ('no_rus', 'Английский'),
    ('rus_sub', 'Русский (субтитры)'),
    ('rus_voice', 'Русский (озвучка)'),
)


def get_path_and_name(instance, filename):
    return f'image_product/{instance.year}/{instance.slug}{splitext(filename)[-1]}'


class Requirement(models.Model):
    title_game = models.CharField(max_length=255)
    CPU = models.CharField(max_length=255)
    video_card = models.CharField(max_length=255)
    RAM = models.CharField(max_length=255)

    def __str__(self):
        return f'Requirements {self.title_game}'


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    poster = models.ImageField(upload_to=get_path_and_name, blank=True)

    description = models.TextField()
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(max_length=100, choices=RUS_LANGUAGE)
    year = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolut_url(self):
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def save(self):
        super().save()
        if self.poster:
            img = Image.open(self.poster.path)
            output_size = (700, 500)
            img.thumbnail(output_size)
            img.save(self.poster.path)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255, unique=True)
    product = models.ManyToManyField(Product, related_name='product_genre', blank=True)

    def __str__(self):
        return self.name
