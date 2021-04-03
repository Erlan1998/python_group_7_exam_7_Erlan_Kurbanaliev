# Создайте модель Опроса (Poll) со следующими полями:
#
# Вопрос - текстовое, обязательное.
# Дата и время создания опроса - автозаполнение.
#
# Создайте модель Варианта ответа (Choice) со следующими полями:
#
# Текст варианта - текстовое, обязательное.
# Опрос - внешний ключ, если удаляется опрос - его варианты ответа тоже удаляются.
#
# Зарегистрируйте модели в админ-панели и добавьте тестовые данные, создайте фикстуру.


from django.db import models
# from webapp.validators import MinLengthValidator, CapitalLetter, OnlyLetters


class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голосы'

    def __str__(self):
        return f'{self.question}'

class Choice(models.Model):
    answer = models.TextField(max_length=200, null=False, blank=False)
    poll = models.ForeignKey('webapp.Poll', related_name='Choices', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Choices'
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'

    def __str__(self):
        return f'{self.id}. {self.answer}: {self.poll}'