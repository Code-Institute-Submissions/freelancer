# Generated by Django 3.0.5 on 2020-04-13 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_auto_20200413_1819'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='Uploads',
        ),
    ]