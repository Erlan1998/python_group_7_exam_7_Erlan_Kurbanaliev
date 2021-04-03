from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm
# from django.urls import reverse



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
