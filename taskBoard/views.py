from django.db.models import fields
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request, HttpRequest, response
from django.template.defaultfilters import title
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from taskBoard.forms import TaskCreateForm
from django.contrib.auth.models import User, UserManager

from .models import Task
from taskBoard import models
from taskBoard.forms import TaskCreateForm


class IndexView(LoginRequiredMixin, ListView, FormView):
    template_name = 'taskBoard/index.html'
    content_object_name = 'task_list'
    paginate_by = 10
    form_class = TaskCreateForm

    def get_context_data(self, **kwargs):
        if self.request.POST:
            self.extra_context = {'title': self.request.POST['title'],
                                  'create_by': self.request.POST['create_by'],
                                  'status': self.request.POST['status']}
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        if self.request.POST:
            list_filter = Task.objects.all()
            if self.request.POST['title']:
                list_filter = list_filter.filter(
                    title__icontains=self.request.POST['title'])
            if self.request.POST['create_by']:
                list_filter = list_filter.filter(
                    create_by=self.request.POST['create_by'])
            if self.request.POST['status']:
                list_filter = list_filter.filter(
                    status__icontains=self.request.POST['status'])
            return list_filter
        else:
            return Task.objects.all()

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DetailEdit(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'status']
    template_name = 'taskBoard/detail.html'
    success_url = '/taskBoard/'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'taskBoard/add.html'
    success_url = '/taskBoard/'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/taskBoard/'


@ login_required(redirect_field_name='taskBoard')
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.description = request.POST['description']
    task.title = request.POST['title']
    if not task.status == request.POST['status'] and request.POST['status'] == 'CLOSED':
        task.date_close = datetime.now()
    elif not task.status == request.POST['status'] and task.status == 'CLOSED':
        task.date_close = None
    task.status = request.POST['status']
    task.save()
    return HttpResponseRedirect(reverse('taskBoard:index'))


@ login_required(redirect_field_name='taskBoard')
def createTask(request):
    task = Task()
    task.description = request.POST['description']
    task.title = request.POST['title']
    task.status = 'NEW'
    task.date_create = datetime.now()
    task.create_by = request.user
    task.save()
    return HttpResponseRedirect(reverse('taskBoard:index'))
