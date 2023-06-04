from django.urls import path

from main.views import contacts, IndexListView, BlogListView, BlogDetailView,\
    BlogCreateView, BlogUpdateView, BlogDeleteView

from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create_post'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update_post'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete_post'),
]
