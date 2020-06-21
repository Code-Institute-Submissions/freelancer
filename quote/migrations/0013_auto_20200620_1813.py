# Generated by Django 3.0.5 on 2020-06-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0012_auto_20200620_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.CharField(choices=[('Deleted', 'Deleted'), ('Pending', 'Pending'), ('Ready', 'Done'), ('Accepted', 'Accepted')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='quotefiles',
            name='status',
            field=models.CharField(choices=[('Deleted', 'Deleted'), ('Pending', 'Pending'), ('Ready', 'Done'), ('Accepted', 'Accepted')], default='Pending', max_length=100),
        ),
    ]
