from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import validate_name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), validate_name],

    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True,
    )