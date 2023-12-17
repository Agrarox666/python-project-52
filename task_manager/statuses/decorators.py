from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from task_manager.tasks.models import Task


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.warning(request,
                             message=_("You are not authorized! Please log in"),  # noqa: E501
                             extra_tags='danger')
            return redirect("login")
        else:
            status_id = kwargs['pk']
            tasks = Task.objects.filter(status=status_id)

            perm = list(tasks) == []
            if not perm:
                messages.warning(request,
                                 message=_("Cannot remove status because it is in use"),  # noqa: E501
                                 extra_tags='danger')
                return redirect('statuses_index')
            else:
                return fn(request, *args, **kwargs)

    return wrapper
