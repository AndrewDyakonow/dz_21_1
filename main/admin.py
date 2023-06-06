from django.contrib import admin

from main.models import Category, Product, Blogs


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'header', 'slug', 'content', 'image', 'create_data', 'sign', 'views', 'is_active')
    prepopulated_fields = {'slug': ('header',)}
