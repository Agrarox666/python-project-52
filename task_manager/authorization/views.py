from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from task_manager.authorization.forms import LoginForm


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        messages.success(self.request, _('You are logged in'))
        return reverse_lazy('main')


class LogoutUserView(LogoutView):

    def get_success_url(self):
        messages.info(self.request, _('You are logged out'))
        return reverse_lazy('main')
