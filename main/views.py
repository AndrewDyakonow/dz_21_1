from django.shortcuts import render

from main.models import Product


def index(request):
    products_for_all = Product.objects.all()
    context = {
        'object_list': products_for_all
    }
    return render(request, 'main/index.html', context)
