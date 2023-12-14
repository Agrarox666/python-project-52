from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from task_manager.decorators import CustomLoginRequiredMixin
from task_manager.forms import CreationForm, LoginForm, UpdatingForm
from task_manager.models import TaskUser
from django.contrib import messages


def index(request):
    a = None
    a.hello()  # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')


class UsersIndexView(View):
    def get(self, request, *args, **kwargs):
        users = TaskUser.objects.all()
        context = {'users': users}
        return render(request, 'users_index.html', context)


class UserCreateView(CreateView):
    form_class = CreationForm
    template_name = 'user_create.html'

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return reverse_lazy('login')


class UserUpdateView(CustomLoginRequiredMixin, UpdateView):
    form_class = UpdatingForm
    template_name = 'user_update.html'
    model = TaskUser
    success_url = reverse_lazy('get_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно изменен')
        return reverse_lazy('users_index')


class UserDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = TaskUser
    template_name = 'user_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно удалён')
        return reverse_lazy('users_index')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        messages.success(self.request, 'Вы залогинены')
        return reverse_lazy('main')


class LogoutUserView(LogoutView):

    def get_success_url(self):
        messages.info(self.request, 'Вы разлогинены')
        return reverse_lazy('main')


class LabelView(View):
    pass
