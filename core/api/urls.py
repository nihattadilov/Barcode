
from django.urls import path
from .views import (
    BlogListAPIView, BlogDetailAPIView, BlogCreateAPIView, BlogUpdateAPIView, BlogDeleteAPIView
)

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blog-list'),
    path('blogs/<int:id>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('blogs/create/', BlogCreateAPIView.as_view(), name='blog-create'),
    path('blogs/<int:id>/update/', BlogUpdateAPIView.as_view(), name='blog-update'),
    path('blogs/<int:id>/delete/', BlogDeleteAPIView.as_view(), name='blog-delete'),
]
