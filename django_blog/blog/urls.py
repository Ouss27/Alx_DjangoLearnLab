from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import custom views from blog app

urlpatterns = [
    # Login and logout views using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html', next_page='login'), name='logout'),

    # Custom views for registration and profile management
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.post_list, name='posts'),  # URL for blog posts
]
