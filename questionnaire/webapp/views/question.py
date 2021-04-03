from django.core.paginator import Paginator
from webapp.forms import PollForm, SearchForm
from django.views.generic import CreateView, ListView,  UpdateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.models import Poll
from django.db.models import Q
from django.utils.http import urlencode


class IndexViewQuestion(ListView):
    template_name = 'question/index_question.html'
    model = Poll
    context_object_name = 'polls'
    ordering = '-created_date'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexViewQuestion, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(question__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['search_form'] = self.form

        if self.search_data:
            kwargs['query'] = urlencode({'search_value': self.search_data})

        return kwargs


class QuestionView(DetailView):
    template_name = 'question/view_question.html'
    model = Poll
    pk_url_kwarg = 'id'
    context_object_name = 'poll'
    # paginate_by = 3


class QuestionCreate(CreateView):
    template_name = 'question/create_question.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll', kwargs={'id': self.object.id})


class QuestionUpdateView(UpdateView):
    template_name = 'question/update_question.html'
    model = Poll
    form_class = PollForm
    context_object_name = 'poll'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('poll', kwargs={'id': self.object.id})

class QuestionDeleteView(DeleteView):
    template_name = 'question/delete.html'
    model = Poll
    context_object_name = 'poll'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index_question')



