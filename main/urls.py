from django.urls import path

from main.views import contacts, IndexListView, BlogListView, BlogDetailView,\
    BlogCreateView, BlogUpdateView, BlogDeleteView

from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/create/<slug:slug>', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<slug:slug>', BlogUpdateView.as_view(), name='blog_update_post'),
    path('blog/delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete_post'),
]
