from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    image = models.ImageField(upload_to='image/')
    category = models.CharField(max_length=25)
    price = models.IntegerField
    date_create = models.DateTimeField
    date_of_change = models.DateTimeField

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)
