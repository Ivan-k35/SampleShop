# Generated by Django 3.2.9 on 2022-01-26 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='sd',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='sd_volume_max',
        ),
    ]
