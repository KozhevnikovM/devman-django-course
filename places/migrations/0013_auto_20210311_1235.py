# Generated by Django 3.1.7 on 2021-03-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20210311_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Номер фотографии в списке'),
        ),
    ]
