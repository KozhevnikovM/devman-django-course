# Generated by Django 3.1.7 on 2021-03-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
