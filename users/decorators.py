from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.warning(request,
                             message=_("You are not authorized! Please log in"),  # noqa: E501
                             extra_tags='danger')
            return redirect("login")
        else:
            perm = request.user.id == kwargs['pk']
            if not perm:
                messages.warning(request,
                                 message=_("You do not have permission to change another user"),  # noqa: E501
                                 extra_tags='danger')
                return redirect('users_index')
            else:
                return fn(request, *args, **kwargs)

    return wrapper
