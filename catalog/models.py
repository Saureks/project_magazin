

from django.db import models

# Create your models here.

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    image = models.ImageField(upload_to="catalog/", **NULLABLE, verbose_name="Превью")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    purchase_price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    # manufactured_at = models.DateField(**NULLABLE, verbose_name="Дата производства продукта")

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.purchase_price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    version_number = models.PositiveIntegerField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, **NULLABLE, verbose_name="Название версии")
    is_actual = models.BooleanField(default=False, verbose_name="Текущая версия")

    def __str__(self):
        return f"{self.version_number} ({self.version_name}) - {self.product}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
