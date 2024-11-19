from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Book, Author, Library, Librarian

# Create your views here.

def book_list(request):
    books = Book.objects.select_related('author').all() # Fetch books and related authors efficiently
    return render(request, 'book_list.html',{'books': books})

class LibraryDetailView(DetailView):
    model=Library
    template_name='library_detail.html'
    context_object_name='library'
    