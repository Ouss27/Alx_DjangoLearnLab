from bookshelf.models import Book 

# retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# delete all books created
book.delete()

# confirm that all books are deleted
Book.objects.all()

# Expected output
<QuerySet []>


 