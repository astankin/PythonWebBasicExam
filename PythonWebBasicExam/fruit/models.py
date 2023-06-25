from django.core.validators import MinLengthValidator
from django.db import models

from PythonWebBasicExam.fruit.validators import fruit_name_validator


# Create your models here.

class FruitModel(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            fruit_name_validator,
        ]
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )
    description = models.TextField()
    nutrition = models.TextField(
        null=True,
        blank=True,
    )
