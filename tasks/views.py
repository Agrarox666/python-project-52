from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView

from tasks.decorators import CustomLoginRequiredMixin
from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.
class TaskView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks_index.html', {'tasks': tasks})


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'

    def get_success_url(self):
        messages.success(self.request, 'Задача успешно создана')
        return reverse_lazy('tasks_index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskShowView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        labels = task.labels.all()
        return render(request, 'task_show.html', {'task': task, 'labels': labels})


class TaskUpdateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_update.html', {'form': form, 'task': task})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Задача успешно изменена')
            return redirect('tasks_index')
        else:
            return render(request, 'task_update.html', {'form': form, 'task': task})


class TaskDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Задача успешно удалена')
        return reverse_lazy('tasks_index')
