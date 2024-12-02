from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book, Author, Librarian
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


# Create your views here.

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all() 
    return render(request, 'relationship_app/list_books.html',{'books': books})
    
    

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model=Library
    template_name='relationship_app/library_detail.html'
    context_object_name='library'

# Class-based view for user registration
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Redirect to login page after successful signup
    template_name = 'relationship_app/register.html'



# Define the 'register' view
#def register(request):
 #   return render(request, 'relationship_app/register.html')  
