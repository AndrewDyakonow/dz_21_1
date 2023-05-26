from django.core.management import BaseCommand
from datetime import datetime
from main.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {
                'name': 'Orange',
                'description': 'Апельсин',
                'image': 'screenshotes/img.png',
                'category': 'Fruits',
                'price': '14',
                'date_create': datetime.now()
            },
            {
                'name': 'Potato',
                'description': 'Картофель',
                'image': 'screenshotes/img.png',
                'category': 'Plants',
                'price': '53',
                'date_create': datetime.now()
            },
            {
                'name': 'Tomato',
                'description': 'Томат',
                'image': 'screenshotes/img.png',
                'category': 'Plants',
                'price': '43',
                'date_create': datetime.now()
            }
        ]

        products_for_add = []
        for product in product_list:
            products_for_add.append(Product(**product))

        Product.objects.bulk_create(products_for_add)
