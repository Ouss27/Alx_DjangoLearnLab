from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .views import role_check

# Member View
@user_passes_test(role_check('Member'))
def member_view(request):
    return HttpResponse("Welcome, Member! You have access to this view.")