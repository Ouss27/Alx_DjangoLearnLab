from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def role_check(role):
    def check_user(user):
        return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == role
    return check_user

@user_passes_test(role_check('Admin'))
def admin_view(request):
    return HttpResponse("Welcome, Admin! You have access to this view.")
