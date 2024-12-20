"""
URL configuration for django-models project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.views.generic import TemplateView


urlpatterns = [

    path('book/', list_books, name='book'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    
     # Built-in views for authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
     # Custom view for registration
    path('register/', views.SignUpView.as_view(), name='register'),

    # path('accounts/', include('django.contrib.auth.urls')),
    # is part of Django's built-in authentication system. When included,
    #  it automatically adds a set of URL patterns for common authentication-related views,
    #  such as login, logout, password reset, etc.
   
    path('accounts/profile/',TemplateView.as_view(template_name='relationship_app/profile.html'),name='profile'),

    #Path for Roles
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    #Paths for Book(add, edit, delete)
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    
]
