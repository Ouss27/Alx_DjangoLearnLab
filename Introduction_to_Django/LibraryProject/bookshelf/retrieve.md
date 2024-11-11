 from bookshelf.models import Book
 
 # retrieve the book just created
 book1=Book.objects.get(pk=1)

 # Display all attributes
>>> print(book1.title)
1984
>>> print(book1.author)
George Orwell
>>> print(book1.publication_year)
1949
