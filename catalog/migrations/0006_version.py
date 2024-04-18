# Generated by Django 5.0.2 on 2024-04-18 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.PositiveIntegerField(verbose_name='Номер версии')),
                ('version_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название версии')),
                ('is_actual', models.BooleanField(default=False, verbose_name='Текущая версия')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]