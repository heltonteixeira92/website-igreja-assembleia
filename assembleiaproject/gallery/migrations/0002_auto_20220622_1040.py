# Generated by Django 3.2.12 on 2022-06-22 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('slug', models.SlugField(max_length=128, verbose_name='slug')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('album', 'title')},
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_image', to='gallery.album', verbose_name='album'),
        ),
    ]
