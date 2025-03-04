
from rest_framework.generics import(
     ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
)
from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .serialisers import BlogSerialiser
from core.models import Blog


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiser
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    

class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiser
    lookup_field = 'id'


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiser
    
    
class BlogUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiser
    lookup_field = 'id'
    
    
class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiser
    lookup_field = 'id'