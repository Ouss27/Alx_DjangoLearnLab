from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
     path('api/', include('posts.urls')),  # Include posts app URLs under the 'api/' path
    path('api-auth/', include('rest_framework.urls')),  # For browsable API authentication
     path('api/token/', auth_views.obtain_auth_token),  # Add this line for token authentication
]
