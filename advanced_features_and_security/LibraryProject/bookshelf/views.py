from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import ExampleForm


#check for prmission to View Book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request):
    # Safely retrieve all book instances
    instances = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'instances': instances})


# Check for permission to add a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  # Safely save data using Django forms
            return HttpResponse("Book created successfully!")
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})


# Check for permission to edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Safely retrieve the book instance or return a 404 error
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Safely save changes
            return HttpResponse("Book edited successfully!")
    else:
        form = ExampleForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})


# Check for permission to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Safely retrieve the book instance or return a 404 error
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()  # Safely delete the instance
        return HttpResponse("Book deleted successfully!")
    return render(request, 'bookshelf/delete_book.html', {'book': book})