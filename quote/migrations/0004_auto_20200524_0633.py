# Generated by Django 3.0.5 on 2020-05-24 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_auto_20200524_0631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotefiles',
            old_name='file_name',
            new_name='file_names',
        ),
    ]
