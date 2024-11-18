from django.db.models import Prefetch
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Some Author Name"  # Replace with the actual author's name
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)  # Use explicit filter for books by this author
    print(f"Books by {author_name}: {[book.name for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"Author with name '{author_name}' does not exist.")


# List all books in a library
library_name = "Some Library Name"  # Replace with the actual library name
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()  # Access all books through the ManyToManyField
    print(f"Books in {library_name}: {[book.name for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"Library with name '{library_name}' does not exist.")

# Retrieve the librarian for a library
try:
    librarian = library.librarian  # Access the librarian via the OneToOneField
    print(f"Librarian for {library_name}: {librarian.name}")
except AttributeError:
    print(f"No librarian assigned to the library '{library_name}'.")
