from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

import json, os

from ...models import Category, Product

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name), mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('category.json')

        Category.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk') # сохраняем id категорий чтобы они перешли как были в продукты
            new_category = Category(**cat)
            new_category.save()

        products = load_from_json('product.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            # Получаем категорию
            _category = Category.objects.get(id=category)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()