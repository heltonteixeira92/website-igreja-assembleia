# Generated by Django 3.2.12 on 2022-07-26 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_image_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('album', 'title'), 'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
    ]
