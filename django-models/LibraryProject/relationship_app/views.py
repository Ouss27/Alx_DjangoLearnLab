from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book, Author, Librarian
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test


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


# Role Check Function
def role_check(role):
    def check_user(user):
        return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == role
    return check_user

# Admin View
@user_passes_test(role_check('Admin'))
def admin_view(request):
    return HttpResponse("Welcome, Admin! You have access to this view.")

# Librarian View
@user_passes_test(role_check('Librarian'))
def librarian_view(request):
    return HttpResponse("Welcome, Librarian! You have access to this view.")




# Define the 'register' view
#def register(request):
 #   return render(request, 'relationship_app/register.html')  
