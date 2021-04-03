from django import forms
from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['question']


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['answer']


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['choice']