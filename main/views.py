from django.views import generic

from django.shortcuts import render
from django.urls import reverse_lazy

from main.models import Product, Blogs


class IndexListView(generic.ListView):
    model = Product


def contacts(request):
    return render(request, 'main/contacts.html')


class BlogListView(generic.ListView):
    model = Blogs


class BlogDetailView(generic.DetailView):
    model = Blogs


class BlogCreateView(generic.CreateView):
    model = Blogs
    fields = ('header', 'slug', 'content', 'sign', 'image')
    success_url = reverse_lazy('main:blogs')


class BlogUpdateView(generic.UpdateView):
    model = Blogs
    fields = ('header', 'slug', 'content', 'sign', 'image')
    success_url = reverse_lazy('main:blogs')


class BlogDeleteView(generic.DeleteView):
    model = Blogs
    success_url = reverse_lazy('main:blogs')
