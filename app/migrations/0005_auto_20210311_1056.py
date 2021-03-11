# Generated by Django 3.1.7 on 2021-03-11 07:56

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210311_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='details_description_long',
            field=tinymce.models.HTMLField(verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='details_description_short',
            field=models.CharField(max_length=400, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='details_lat',
            field=models.FloatField(verbose_name='Координата по широте'),
        ),
        migrations.AlterField(
            model_name='place',
            name='details_lng',
            field=models.FloatField(verbose_name='Координата по долготе'),
        ),
        migrations.AlterField(
            model_name='place',
            name='details_title',
            field=models.CharField(max_length=200, verbose_name='Название места'),
        ),
    ]
