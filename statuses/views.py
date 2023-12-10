from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView

from statuses.forms import CreateStatus, UpdateStatus
from statuses.models import Status


# Create your views here.
class StatusView(View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        context = {'statuses': statuses}
        return render(request, 'statuses_index.html', context)


class StatusCreateView(CreateView):
    model = Status
    form_class = CreateStatus
    template_name = 'status_create.html'

    def get_success_url(self):
        messages.success(self.request, 'Статус успешно создан')
        return reverse_lazy('statuses_index')


class StatusUpdateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = UpdateStatus(instance=status)
        return render(request, 'status_update.html', {'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = UpdateStatus(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Статус успешно изменен')
            return redirect('statuses_index')
        else:
            return render(request, 'status_update.html', {'form': form, 'status': status})


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Статус успешно удалён')
        return reverse_lazy('statuses_index')
