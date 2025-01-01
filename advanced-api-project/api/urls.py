from django.urls import path
from api.views import BookCreateView, BookDetailView, BookDeleteView, BookListView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view, name= 'books_list'),
    path('book/<int:pk>/', BookDetailView.as_view, name= 'book_detail'),
    path('books/create/', BookCreateView.as_view, name= 'books_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view, name= 'books_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view, name= 'books_delete'),
]

