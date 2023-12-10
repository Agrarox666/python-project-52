from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from tasks.models import Task


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.warning(request,
                             message="Вы не авторизованы! Пожалуйста, выполните вход",  # noqa: E501
                             extra_tags='danger')
            return redirect("login")
        else:
            task_id = kwargs['pk']
            task = Task.objects.get(id=task_id)
            owner_id = task.author.id
            perm = request.user.id == owner_id
            print(task_id, task, task.__dict__, perm)
            if not perm:
                messages.warning(request,
                                 message="Задачу может удалить только её автор",  # noqa: E501
                                 extra_tags='danger')
                return redirect('tasks_index')
            else:
                return fn(request, *args, **kwargs)

    return wrapper


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Custom mixin for warning message if the user wants to delete a task that is not his own."""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
