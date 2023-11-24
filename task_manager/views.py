from django.shortcuts import render
from django.utils.translation import gettext


def main(request):
    context = {
        'app_name': gettext('Task Manager'),
        'users': gettext('Users'),
        'log_in': gettext('Log in'),
        'sign_in': gettext('Sign in'),
    }
    return render(request, 'main.html', context)
