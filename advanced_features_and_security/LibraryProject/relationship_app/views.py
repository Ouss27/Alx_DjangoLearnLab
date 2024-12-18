from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library, Book, Author, Librarian
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required


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


# Check if user is Admin
def is_admin(user):
    return user.profile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Check if user is Librarian
def is_librarian(user):
    return user.profile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# Check if user is Member
def is_member(user):
    return user.profile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


#Add Book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return HttpResponse("Book added successfully!")
    return render(request, 'relationship_app/add_book.html')

#Edit Book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return HttpResponse("Book updated successfully!")
    return render(request, 'relationship_app/edit_book.html', {'book': book})

#Delete Book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return HttpResponse("Book deleted successfully!")
    return render(request, 'relationship_app/delete_book.html', {'book': book})





