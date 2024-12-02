from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .views import role_check

# Admin View
@user_passes_test(role_check('Admin'))
def admin_view(request):
    return HttpResponse("Welcome, Admin! You have access to this view.")