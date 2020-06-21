# Generated by Django 3.0.5 on 2020-06-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0010_auto_20200620_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotefiles',
            name='status',
            field=models.CharField(choices=[('DELETED', 'Deleted'), ('PENDING', 'Pending'), ('DONE', 'Done'), ('ACCEPTED', 'Accepted')], default='PENDING', max_length=100),
        ),
    ]
