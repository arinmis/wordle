from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Word(models.Model):

    class Language(models.TextChoices):
        EN = 'tr', _('Turkish')
        TR = 'en', _('English')

    lang = models.CharField(max_length=2, choices=Language.choices)
    word = models.CharField(max_length=200)
