from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('products/', views.products, name='blog-product'),
    path('products/product/<int:pk>/',
         ProductDetailView.as_view(), name='product-detail'),
    path('products/product/new/', ProductCreateView.as_view(), name='product-create'),
    path('products/product/<int:pk>/update/',
         ProductUpdateView.as_view(), name='product-update'),
    path('products/product/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product-delete'),
]
