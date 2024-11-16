from django.db.models import Prefetch
from relationship_app.models import Author, Book, Library, Librarian

authors_with_books = Author.objects.prefetch_related(
        Prefetch('books', queryset=Book.objects.all()))

 


libraries_with_books = Library.objects.prefetch_related(
        Prefetch('books', queryset=Book.objects.select_related('author')))




libraries_with_librarian = Library.objects.select_related('librarian')
