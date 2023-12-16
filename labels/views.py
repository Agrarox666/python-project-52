from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.utils.translation import gettext as _
from labels.decorators import login_required
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
        messages.success(self.request, _('Label created successfully'))
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
            messages.success(self.request, _('Label changed successfully'))
            return redirect('labels_index')
        else:
            return render(request, 'label_update.html', {'form': form, 'label': label})


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label_delete.html'

    def get_success_url(self):
        messages.success(self.request, _('Label removed successfully'))
        return reverse_lazy('labels_index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
