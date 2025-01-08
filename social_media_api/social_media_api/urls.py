from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),  # Include posts app URLs under the 'api/' path
    path('api-auth/', include('rest_framework.urls')),  # For browsable API authentication
    path('api/login/', obtain_auth_token, name='api_login'),  # Token-based login endpoint
]


