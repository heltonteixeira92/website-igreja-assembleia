from django.contrib import admin
from .models import Image, Album


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('icon', 'created', )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created', )
    readonly_fields = ('icon',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
