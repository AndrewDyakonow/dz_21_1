from django.utils.timezone import now
from django.db import models


def get_date():
    return now()


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    description = models.CharField(max_length=25, verbose_name='Описание')
    image = models.ImageField(upload_to='image/')
    category = models.CharField(max_length=25, verbose_name='Категория')
    price = models.IntegerField(default=0, verbose_name='Цена')
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_of_change = models.DateTimeField

    def __str__(self):
        return f'{self.name}, {self.description}, {self.category}, {self.price}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    description = models.CharField(max_length=25, verbose_name='Описание')

    def __str__(self):
        return self.name, self.description

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)



