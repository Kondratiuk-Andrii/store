# Generated by Django 3.2.13 on 2023-05-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'basket', 'verbose_name_plural': 'baskets'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default=0, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]