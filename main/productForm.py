from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('date_of_change', 'date_create', 'date_of_change')

