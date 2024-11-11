from bookshelf.models import Book 

# delete all books created
Book.objects.all().delete()

# confirm that all books are deleted
Book.objects.all()

# Expected output
<QuerySet []>


 