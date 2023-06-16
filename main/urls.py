from django.urls import path

from main.views import contacts, ProductListView, BlogListView, BlogDetailView,\
    BlogCreateView, BlogUpdateView, BlogDeleteView, ProductCreateView

from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/create/<slug:slug>', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<slug:slug>', BlogUpdateView.as_view(), name='blog_update_post'),
    path('blog/delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete_post'),
]
