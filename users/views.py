from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from task_manager.decorators import CustomLoginRequiredMixin
from task_manager.forms import CreationForm, UpdatingForm
from users.models import TaskUser


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
