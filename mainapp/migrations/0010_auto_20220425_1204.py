# Generated by Django 3.2.9 on 2022-04-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20220425_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=False, verbose_name='Наличие карты памяти'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем карты памяти'),
        ),
    ]
