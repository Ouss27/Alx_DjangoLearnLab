from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library, Book, Author, Librarian
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView




# Create your views here.

def list_books(request):
    books = Book.objects.all() 
    return render(request, 'relationship_app/list_books.html',{'books': books})
    
    


class LibraryDetailView(DetailView):
    model=Library
    template_name='relationship_app/library_detail.html'
    context_object_name='library'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    