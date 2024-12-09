from django.contrib import admin
from django.urls import path, include  # Import include to reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include URLs from our relationship_app
]
