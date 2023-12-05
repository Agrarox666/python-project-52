from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            messages.warning(request,
                             message="Вы не авторизованы! Пожалуйста, выполните вход.",  # noqa: E501
                             extra_tags='danger')
            return redirect("login")
        else:
            perm = request.user.id == kwargs['pk']
            if not perm:
                messages.warning(request,
                                 message="У вас нет прав для изменения другого пользователя.",  # noqa: E501
                                 extra_tags='danger')
                return redirect('get_users')
            else:
                return fn(request, *args, **kwargs)

    return wrapper


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Custom mixin for warning message if user isn't authenticated."""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
