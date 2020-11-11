from django.db import models


class Quest(models.Model):
    text = models.TextField(max_length=100, blank=False, verbose_name='Вопрос')
    survey = models.ForeignKey('MySurvey', on_delete=models.PROTECT, verbose_name='Опрос')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['survey']

    def __str__(self):
        return self.text

class MySurvey(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название', db_index=True)
    published = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    end = models.DateField(auto_now_add=False, verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


    def __str__(self):
        return self.title


class Users(models.Model):
    answer = models.CharField(max_length=200, blank=True, verbose_name='Ответ', db_index=True)
    qwes = models.ForeignKey('Quest', default=1, on_delete=models.CASCADE, verbose_name='Вопрос')
    sur = models.ForeignKey('MySurvey', default=1, on_delete=models.CASCADE, verbose_name='Опрос')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer

