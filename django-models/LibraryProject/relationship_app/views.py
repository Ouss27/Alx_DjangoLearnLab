from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library, Book, Author, Librarian

# Create your views here.

def book_list(request):
    books = Book.objects.all() 
    return render(request, 'relationship_app/list_books.html',{'books': books})
    
    


class LibraryDetailView(DetailView):
    model=Library
    template_name='relationship_app/library_detail.html'
    context_object_name='library'
    