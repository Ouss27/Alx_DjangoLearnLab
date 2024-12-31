from django.db import models
from datetime import datetime



class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField(max_length=4, default=datetime.now().year)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')