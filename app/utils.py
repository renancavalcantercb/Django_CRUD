from django.contrib import messages
from django.shortcuts import redirect


def auth_required_message(request):
    messages.get_messages(request)
    message = 'You must be logged in to access this page'
    div_class = 'alert alert-danger'
    messages.warning(request, message, extra_tags=div_class)
    return redirect('login')
