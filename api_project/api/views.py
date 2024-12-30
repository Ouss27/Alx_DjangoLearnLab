from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class BookList(generics.ListAPIView):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
   # permission_classes = [IsAuthenticated] ## Only authenticated users can access this view
   # permission_classes = [IsAdminUser] ## Only admin users can access this view
    permission_classes = [IsAuthenticatedOrReadOnly] ## read-only access to unauthenticated users and full access to authenticated users