from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

#Set Up Test Data
class BookAPITestCase(TestCase):
    def setUp(self):
        # Initialize APIClient for sending API requests
        self.client = APIClient()
        
        # Define sample data for a book
        self.book_data = {
            'title': 'Test Book', 
            'author': 'Test Author', 
            'published_year': 2023
        }
      # Create a book instance in the test database
        self.book = Book.objects.create(**self.book_data)

#Test Create Operation

    def test_create_book(self):
        # Send a POST request to create a new book
        response = self.client.post(reverse('book-list'), data={
            'title': 'New Book',
            'author': 'New Author',
            'published_year': 2024
        })
        
        # Check if the response status is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify that a new book is added to the database
        self.assertEqual(Book.objects.count(), 2)

#Test Read Operation

    def test_read_book(self):
        # Send a GET request to retrieve details of the created book
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.id}))
        
        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate that the returned title matches the created book's title
        self.assertEqual(response.data['title'], self.book_data['title'])

#Test Update Operation

    def test_update_book(self):
        # Send a PUT request to update the book details
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), data={
            'title': 'Updated Title',
            'author': 'Updated Author',
            'published_year': 2025
        })
        
        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Reload the book instance from the database
        self.book.refresh_from_db()
        
        # Validate that the title is updated in the database
        self.assertEqual(self.book.title, 'Updated Title')

#Test Delete Operation

    def test_delete_book(self):
        # Send a DELETE request to remove the book
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.id}))
        
        # Check if the response status is 204 (No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify that the book is deleted from the database
        self.assertEqual(Book.objects.count(), 0)

#Test Filtering

    def test_filter_books(self):
        # Send a GET request with a filter for author
        response = self.client.get(reverse('book-list') + '?author=Test Author')
        
        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure at least one book matches the filter
        self.assertTrue(len(response.data) > 0)

#Test Searching

    def test_search_books(self):
        # Send a GET request with a search query
        response = self.client.get(reverse('book-list') + '?search=Test')
        
        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#Test Ordering

    def test_order_books(self):
        # Send a GET request to order books by published year in descending order
        response = self.client.get(reverse('book-list') + '?ordering=-published_year')
        
        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#Test Unauthorized Access

    def test_unauthorized_access(self):
        # Log out the user to simulate an unauthenticated request
        self.client.logout()
        
        # Attempt to access a protected resource
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.id}))
        
        # Check if the response status is 403 (Forbidden)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)