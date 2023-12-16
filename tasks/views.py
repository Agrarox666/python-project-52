from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.utils.translation import gettext as _

from tasks.decorators import CustomLoginRequiredMixin
from tasks.filter import TaskFilter, CheckBox
from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.
class TaskView(View):

    def get(self, request, *args, **kwargs):
        author = request.GET.get('self_tasks', False)
        if author:
            author_tasks = Task.objects.filter(author=request.user.id)
            f = TaskFilter(request.GET, queryset=author_tasks)
            c = CheckBox(request.GET)
            return render(request, 'tasks_index.html', {'tasks': f.qs, 'filter': f, 'checkbox': c})

        f = TaskFilter(request.GET, queryset=Task.objects.all())
        c = CheckBox(request.GET)
        return render(request, 'tasks_index.html', {'tasks': f.qs, 'filter': f, 'checkbox': c})


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'

    def get_success_url(self):
        messages.success(self.request, _('Task created successfully'))
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
            messages.success(self.request, _('Task changed successfully'))
            return redirect('tasks_index')
        else:
            return render(request, 'task_update.html', {'form': form, 'task': task})


class TaskDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Task removed successfully'))
        return reverse_lazy('tasks_index')
