from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, 
                    CommentCreateView, CommentUpdateView, CommentDeleteView, SearchView, PostByTagListView)

urlpatterns = [
    # Login and logout views using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html', next_page='login'), name='logout'),

    # Custom views for registration and profile management
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.post_list, name='posts'),  # URL for blog posts

    #CRUD paths
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    #Comments paths
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    #search paths
    path('search/', SearchView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
    
]
