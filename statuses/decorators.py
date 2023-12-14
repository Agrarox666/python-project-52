from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from labels.models import Label
from statuses.models import Status
from tasks.models import Task


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.warning(request,
                             message="Вы не авторизованы! Пожалуйста, выполните вход",  # noqa: E501
                             extra_tags='danger')
            return redirect("login")
        else:
            status_id = kwargs['pk']
            tasks = Task.objects.filter(status=status_id)

            perm = list(tasks) == []
            if not perm:
                messages.warning(request,
                                 message="Невозможно удалить статус, потому что он используется",  # noqa: E501
                                 extra_tags='danger')
                return redirect('statuses_index')
            else:
                return fn(request, *args, **kwargs)

    return wrapper


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Custom mixin for warning message if the user wants to delete a bounded status."""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)