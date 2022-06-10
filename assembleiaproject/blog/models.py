from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(_('title'), max_length=250)
    slug = models.SlugField(_('slug'), max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(_('body'))
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    img = models.ImageField(upload_to='blog_img')
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish', )
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()
ghp_i19hEMvGtuiW82HTgm9DFEQr6RfLkE1Nunt