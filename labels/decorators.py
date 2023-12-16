from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from labels.models import Label


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.warning(request,
                             message=_("You are not authorized! Please log in"),  # noqa: E501
                             extra_tags='danger')
            return redirect("login")
        else:
            label_id = kwargs['pk']
            label = Label.objects.get(id=label_id)
            tasks = label.task_set.all()
            perm = list(tasks) == []
            if not perm:
                messages.warning(request,
                                 message=_("Cannot remove label because it is in use"),  # noqa: E501
                                 extra_tags='danger')
                return redirect('labels_index')
            else:
                return fn(request, *args, **kwargs)

    return wrapper


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Custom mixin for warning message if the user wants to delete a bounded label."""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
