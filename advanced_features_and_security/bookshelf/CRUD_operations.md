# Create

# create a new book instance
b1=Book.objects.create(title="1984",author="George Orwell",publication_year=1949)

# print the new book instance
print(b1)

# expected output
<Book: Book object (1)>


# Retrieve

# retrieve the book just created
 last_book=Book.objects.last()

 # Display all attributes
>>> print(last_book.title)
1984
>>> print(last_book.author)
George Orwell
>>> print(last_book.publication_year)
1949


# Update

# Retrieve the Book instance by its current title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Confirm the update by displaying the new title
print(f"Updated Title: {book.title}")

# Expected output
Updated Title: Nineteen Eighty-Four


# Delete

# delete all books created
Book.objects.all().delete()

# confirm that all books are deleted
Book.objects.all()

# Expected output
<QuerySet []>