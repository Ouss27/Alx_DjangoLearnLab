from django.urls import include, path
from .views import BookList
from rest_framework.routers import DefaultRouter
from api_project.api import views

router = DefaultRouter()
router.register(r'book_all', views.BookViewSet, basename='book_all')



urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Route to the BookList view (ListAPIView)
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]