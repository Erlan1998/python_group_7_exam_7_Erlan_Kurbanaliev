from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm
from django.urls import reverse


class ChoiceAddView(CreateView):
    model = Poll
    template_name = 'choice/add.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('id'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        form.save_m2m()
        return redirect('poll', id=poll.id)


class ChoiceUpdateView(UpdateView):
    template_name = 'choice/update.html'
    model = Choice
    form_class = ChoiceForm
    context_object_name = 'choice'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('poll', kwargs={'id': self.object.poll_id})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/delete.html'
    model = Choice
    context_key = 'choice'
    pk_url_kwarg = 'id'



    def get_success_url(self):
        return reverse('poll', kwargs={'id': self.object.poll_id})
