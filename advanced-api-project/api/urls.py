from django.urls import path
from api.views import BookCreateView, BookDetailView, BookDeleteView, BookListView, BookUpdateView

urlpatterns = [
    path('book/', BookListView.as_view, name= 'book_list'),
    path('book/<int:pk>/', BookDetailView.as_view, name= 'book_detail'),
    path('book/create/', BookCreateView.as_view, name= 'book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view, name= 'book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view, name= 'book_delete'),
]

