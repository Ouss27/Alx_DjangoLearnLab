from bookshelf.models import Book  

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