# Generated by Django 3.0.5 on 2020-04-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0007_auto_20200420_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotefiles',
            name='quote_ref',
            field=models.IntegerField(default=0),
        ),
    ]