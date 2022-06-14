from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify


# Create your models here.
class Image(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(_('title'), max_length=128)
    slug = models.SlugField(_('slug'), max_length=128, blank=True)
    img = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(_('description'), blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True, db_index=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
