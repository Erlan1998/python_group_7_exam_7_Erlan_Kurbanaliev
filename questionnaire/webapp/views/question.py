# from django.core.paginator import Paginator
from webapp.forms import PollForm
from django.views.generic import CreateView, ListView,  UpdateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.models import Poll
# from django.db.models import Q
# from django.utils.http import urlencode

# Этап 2
# Напишите CRUD опросов:
#
# список опросов (главная);
# просмотр опроса;
# создание опроса;
# изменение опроса;
# удаление опроса с подтверждением.
#
# Указания:
#
# В списке опросов отсортируйте опросы по дате создания в убывающем порядке.
# В списке опросов настройте пагинацию для вывода по 5 опросов на странице.


class IndexViewQuestion(ListView):
    template_name = 'question/index_question.html'
    model = Poll
    context_object_name = 'polls'
    ordering = '-created_date'
    # paginate_by = 5
    # paginate_orphans = 1

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



