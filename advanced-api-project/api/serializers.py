from rest_framework import serializers
from api.models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, data):
        current_year = datetime.now().year
        if data > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future. Current year is {current_year}.")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, Read_only=True)

    class Meta:
        medel = Author
        fields = ['name', 'books']

    