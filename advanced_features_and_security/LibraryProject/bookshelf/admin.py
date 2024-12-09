from django.contrib import admin
from .models import UserProfile, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Show user and role in the admin panel
    list_filter = ('role',)         # Add a filter for roles
    search_fields = ('user__username',)  # Enable searching by username

#Custom User

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)




