from django.views import generic
from main.productForm import ProductForm

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.core.mail import send_mail

from main.models import Product, Blogs


class ProductListView(generic.ListView):
    model = Product


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm


def contacts(request):
    return render(request, 'main/contacts.html')


class BlogListView(generic.ListView):
    model = Blogs

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(is_active=True)
        queryset.filter(sign=False)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blogs

    def get_object(self, **kwargs):
        views = super().get_object()
        views.add_view()
        views.save()
        return views


class BlogCreateView(generic.CreateView):
    model = Blogs
    fields = ('header', 'content', 'sign', 'image')
    success_url = reverse_lazy('main:blogs')


class BlogUpdateView(generic.UpdateView):
    model = Blogs
    fields = ('header', 'content', 'sign', 'image')

    def get_success_url(self):  # Создаём функцию, которая даёт возможность пользователю остаться на странице с подробным отображением записи после завершения её редактирования.
        return reverse_lazy(
            "main:blog_item",
            kwargs={"slug": self.object.slug}
        )


class BlogDeleteView(generic.DeleteView):
    model = Blogs
    success_url = reverse_lazy('main:blogs')
