from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.safestring import mark_safe

from PIL import Image as ImagePIL
from django.conf import settings
import os


class PhotoManager(models.Manager):
    def get_queryset(self):
        return super(PhotoManager, self).get_queryset().filter(status='published')


# Create your models here.
class Album(models.Model):
    title = models.CharField(_('title'), max_length=128)
    slug = models.SlugField(_('slug'), max_length=128)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Image(models.Model):
    def album_directory_path(instance, filename):
        img_name = 'album/{0}/{1}'.format(instance.album.slug, filename)
        full_path = os.path.join(settings.MEDIA_ROOT, img_name)

        if os.path.exists(full_path):
            os.remove(full_path)

        return img_name

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    album = models.ForeignKey(Album, on_delete=models.CASCADE,
                              related_name='album_image',
                              verbose_name=_('album'),
                              null=True)
    title = models.CharField(_('title'), max_length=128)
    slug = models.SlugField(_('slug'), max_length=128, blank=True)
    img = models.ImageField(upload_to=album_directory_path)
    description = models.TextField(_('description'), blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True, db_index=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('album', 'title')
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        size = 600, 600

        if self.img:
            pic = ImagePIL.open(self.img.path)
            pic.thumbnail(size, ImagePIL.LANCZOS)
            pic.save(self.img.path)

    def get_absolute_url(self):
        return reverse('gallery:photo_detail', args=[self.slug])

    @mark_safe
    def icon(self):
        if self.img:
            return f'<img width="30px" height="30px" src="/media/{self.img}"  />'
        else:
            return 'No Image Found'

    icon.short_description = 'Imagem'
    icon.allow_tags = True

    objects = models.Manager()
    photopublished = PhotoManager()
