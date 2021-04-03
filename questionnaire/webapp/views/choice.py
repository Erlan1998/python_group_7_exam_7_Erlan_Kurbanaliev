# from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# from webapp.models import List, Projects
# from webapp.forms import ListForm, SearchForm
# from django.urls import reverse
# from django.db.models import Q
# from django.utils.http import urlencode



# Напишите CRUD для вариантов ответа:
# вывод вариантов ответа на странице опроса;
# добавление варианта ответа;
# редактирование варианта ответа;
# удаление варианта ответа с подтверждением.
# Указания:
# Варианты ответа должны выводиться только на странице опроса, у них нет отдельных страниц списка или просмотра.
# При добавлении варианта ответа пользователь не должен выбирать опрос, он должен проставляться автоматически по коду из url.
# Ссылку на добавление варианта ответа выведите на странице опроса.
# Ссылки на редактирование и удаление вариантов ответа выведите рядом с ними.
