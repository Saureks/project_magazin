import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Product, Category


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open("catalog_data.json", encoding="utf-8") as file:
            data = json.load(file)
        return [item for item in data if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        with open("catalog_data.json", encoding="utf-8") as file:
            data = json.load(file)
        return [item for item in data if item["model"] == "catalog.product"]

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE catalog_category, catalog_product RESTART IDENTITY CASCADE;")

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category["pk"],
                         name=category["fields"]["name"],
                         description=category["fields"]["description"])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product["pk"],
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        purchase_price=product["fields"]["purchase_price"])
            )
        Product.objects.bulk_create(product_for_create)

