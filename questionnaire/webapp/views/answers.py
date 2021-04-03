from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from webapp.models import Answer, Choice, Poll
from webapp.forms import AnswerForm


class AnswerAddView(CreateView):
    model = Answer
    template_name = 'answer/add_answer.html'
    form_class = AnswerForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
            form_class.choice = Choice.objects.filter(poll_id=self.kwargs.get('id'))
        return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('id'))
        form = form.save(commit=False)
        form.poll = poll
        form.save()
        return redirect('poll', id=poll.id)

