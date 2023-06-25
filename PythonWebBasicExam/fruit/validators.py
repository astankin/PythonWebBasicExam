import re

from django.core.exceptions import ValidationError


def fruit_name_validator(value):
    if not re.match("^[A-Za-z]*$", value):
        raise ValidationError('Fruit name should contain only letters!')
