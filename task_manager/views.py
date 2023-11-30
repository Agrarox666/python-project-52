from django.shortcuts import render, redirect
from django.utils.translation import gettext
from django.views import View

from task_manager.forms import UserForm
from task_manager.models import User

nav_context = {
    'nav_app_name': gettext('Task Manager'),
    'nav_users': gettext('Users'),
    'nav_log_in': gettext('Log in'),
    'nav_sign_in': gettext('Sign in'),
}


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main.html', nav_context)


class GetUsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        context = {'users': users}
        context.update(nav_context)
        return render(request, 'users.html', context)


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {'form': form}
        context.update(nav_context)
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        context = {'form': form}
        context.update(nav_context)
        return render(request, 'create.html', context)


class UpdateUserView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserForm(instance=user)

        context = {'form': form, 'user_id': user_id}
        context.update(nav_context)
        return render(request, 'update.html', context)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('get_users')
        context = {'form': form, 'user_id': user_id}
        context.update(nav_context)
        return render(request, 'update.html', context)


class DeleteUserView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        context = {'user': user}
        context.update(nav_context)
        return render(request, 'delete.html', context)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('get_users')
