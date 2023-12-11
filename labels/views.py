from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView

from labels.decorators import CustomLoginRequiredMixin
from labels.forms import CreateLabel, UpdateLabel
from labels.models import Label


# Create your views here.
class LabelView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels_index.html', {'labels': labels})


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = CreateLabel
    template_name = 'label_create.html'

    def get_success_url(self):
        messages.success(self.request, 'Метка успешно создана')
        return reverse_lazy('labels_index')


class LabelUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = UpdateLabel(instance=label)
        return render(request, 'label_update.html', {'form': form, 'label': label})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = UpdateLabel(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Метка успешно изменена')
            return redirect('labels_index')
        else:
            return render(request, 'label_update.html', {'form': form, 'label': label})


class LabelDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Метка успешно удалена')
        return reverse_lazy('labels_index')