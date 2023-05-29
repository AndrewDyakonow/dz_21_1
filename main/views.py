from django.shortcuts import render

from main.models import Product


def index(request):
    products_for_all = Product.objects.all()
    context = {
        'object_list': products_for_all
    }
    return render(request, 'main/index.html', context)


def pages(request):
    products_for_all = Product.objects.all()
    context = {
        'object_list': products_for_all
    }
    return render(request, 'main/pages.html', context)


def contacts(request):
    products_for_all = Product.objects.all()
    context = {
        'object_list': products_for_all
    }
    return render(request, 'main/contacts.html', context)
