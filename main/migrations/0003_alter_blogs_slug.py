# Generated by Django 4.2.1 on 2023-06-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogs_product_date_create_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='create_data', verbose_name='slug'),
        ),
    ]
