from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .models import CustomUser, Book
from .models import Book

# Book Model Admin
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    #model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('email', 'is_staff', 'date_of_birth')
    search_fields = ('email',)
    ordering = ('email',)

#admin.site.register(CustomUser, CustomUserAdmin)
