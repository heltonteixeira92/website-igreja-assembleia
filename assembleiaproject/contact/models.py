from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Message(models.Model):
    name = models.CharField(_('name'), max_length=64)
    email = models.EmailField(_('email'))
    message = models.TextField(_('message'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
