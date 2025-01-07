from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
     path('api/', include('posts.urls')),  # Include posts app URLs under the 'api/' path
    path('api-auth/', include('rest_framework.urls')),  # For browsable API authentication
]
