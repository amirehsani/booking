# Generated by Django 4.1.4 on 2022-12-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='about',
            field=models.TextField(default='Airline'),
        ),
    ]
