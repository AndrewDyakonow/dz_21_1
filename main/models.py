from django.utils.timezone import now
from django.db import models

DEFAULT = {
    'blank': True,
    'null': True,
}


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


class Blogs(models.Model):
    """Модель `Блог`"""
    header = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.CharField(max_length=25, verbose_name='slug')
    content = models.TextField(max_length=250, verbose_name='содержимое')
    image = models.ImageField(**DEFAULT, verbose_name='превью')
    create_data = models.DateField(default=now, verbose_name='дата создания')
    sign = models.CharField(max_length=25, verbose_name='признак публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')

    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return f'{self.header}, {self.content}, {self.image}, {self.create_data}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ('-pk',)

