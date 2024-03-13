from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    Image = models.ImageField(upload_to='preview/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='Категория')
    purchase_price = models.CharField(max_length=100, verbose_name='Цена за покупку')
    created_at = models.CharField(max_length=100, verbose_name='Дата создания')
    updated_at = models.CharField(max_length=100, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)
