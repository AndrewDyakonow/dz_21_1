from django.urls import path

from main.views import index, pages, contacts
from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [
    path('', index, name='index'),
    path('pages/', pages),
    path('contacts/', contacts, name='contacts')
]
