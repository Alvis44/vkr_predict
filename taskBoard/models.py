from os import name
from django.db.models.deletion import SET_DEFAULT

from django.http import request
from django.template.defaultfilters import default
import taskBoard
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpRequest


class Task(models.Model):

    LIST_VALUE = [
        ('NEW', 'Новая'),
        ('INWORK', 'В работе'),
        ('PAUSE', 'Отложена'),
        ('CLOSED', 'Закрыта')
    ]

    class Meta:
        permissions = [("can_add_task", "Добавление задачи"),
                       ("can_delete_task", "Удаление задачи"),
                       ("can_edit_task", "Изменение задачи")]

    title = models.CharField('Заголовок', max_length=150)
    description = models.TextField('Описание', blank=True)
    status = models.CharField(
        'Статус', choices=LIST_VALUE, max_length=20, default='NEW')
    date_create = models.DateTimeField('Дата создания')
    date_close = models.DateTimeField('Дата закрытия', blank=True, null=True)
    create_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Автор')

    def view_status(self):
        for key, value in self.LIST_VALUE:
            if key == self.status:
                return value

    def __str__(self):
        return self.title

    def description_view(self):
        list_lines = self.description.split('\n')
        first_line = list_lines[0]
        if len(first_line) <= 30 and len(list_lines) == 1:
            return first_line
        else:
            return self.description.split('\n')[0][:30] + "..."

    def date_close_view(self):
        if self.date_close == None:
            return '---'
        else:
            return self.date_close

class TaskWorkingHours(models.Model):

    taskInWork = models.ForeignKey(Task, on_delete=models.PROTECT, verbose_name='Задача')
    date_from = models.DateTimeField('Дата с')
    date_to = models.DateTimeField('Дата по', blank=True, null=True)
    timeWorked = models.IntegerField('Отработанное время', blank=True, null=True)