from django.contrib import admin
from .models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Show user and role in the admin panel
    list_filter = ('role',)         # Add a filter for roles
    search_fields = ('user__username',)  # Enable searching by username

