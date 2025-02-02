import random

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


def code_generator(length=5):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def get_or_empty(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return []


# This code is not used for this project. It is only to showcase OneToOneFields
class RegistrationProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='registration_profile'
    )

    code = models.CharField(
        help_text='random code used for registration and for password reset',
        max_length=15,
        default=code_generator
    )
    email = models.EmailField(unique=True, default='example@email.com')
    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Registration profile {self.pk}'
