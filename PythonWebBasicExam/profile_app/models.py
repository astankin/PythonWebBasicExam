from django.core.validators import MinLengthValidator
from django.db import models

from PythonWebBasicExam.profile_app.validators import profile_name_validator


# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            profile_name_validator,
        ],
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            profile_name_validator,
        ],
        verbose_name='Last Name'
    )
    email = models.EmailField(
        max_length=40,
    )
    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)]
    )
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=18,
    )