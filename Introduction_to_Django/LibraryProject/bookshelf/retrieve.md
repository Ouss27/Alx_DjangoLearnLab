 from bookshelf.models import Book
 
 # retrieve the book just created
 last_book=Book.objects.last()

 # Display all attributes
>>> print(last_book.title)
1984
>>> print(last_book.author)
George Orwell
>>> print(last_book.publication_year)
1949
