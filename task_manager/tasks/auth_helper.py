from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from task_manager.tasks.models import Task


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.warning(request,
                             message=_("You are not authorized! Please log in"),  # noqa: E501
                             extra_tags='danger'),  # noqa: E501
            return redirect("login")
        else:
            task_id = kwargs['pk']
            task = Task.objects.get(id=task_id)
            owner_id = task.author.id
            perm = request.user.id == owner_id
            if not perm:
                messages.warning(request,
                                 message=_("Only its author can delete a task"),  # noqa: E501
                                 extra_tags='danger')
                return redirect('tasks_index')
            else:
                return fn(request, *args, **kwargs)

    return wrapper
