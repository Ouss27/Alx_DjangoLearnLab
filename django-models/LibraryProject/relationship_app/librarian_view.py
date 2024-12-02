from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .views import role_check

# Librarian View
@user_passes_test(role_check('Librarian'))
def librarian_view(request):
    return HttpResponse("Welcome, Librarian! You have access to this view.")