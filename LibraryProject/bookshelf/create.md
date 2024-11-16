from bookshelf.models import Book

# create a new book instance
b1=Book.objects.create(title="1984",author="George Orwell",publication_year=1949)

# print the new book instance
print(b1)

# expected output
<Book: Book object (1)>