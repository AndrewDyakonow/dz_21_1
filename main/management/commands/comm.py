from django.core.management import BaseCommand

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
            },
            {
                'name': 'Potato',
                'description': 'Картофель',
                'image': 'screenshotes/img.png',
                'category': 'Plants',
                'price': '53',
            },
            {
                'name': 'Tomato',
                'description': 'Томат',
                'image': 'screenshotes/img.png',
                'category': 'Plants',
                'price': '43',
            }
        ]

        products_for_add = []
        for product in product_list:
            products_for_add.append(Product(**product))

        Product.objects.bulk_create(products_for_add)
