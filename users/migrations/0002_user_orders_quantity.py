# Generated by Django 3.2.13 on 2023-06-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='orders_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]