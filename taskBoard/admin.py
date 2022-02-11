from django.contrib import admin

from .models import Task, TaskWorkingHours

admin.site.register(Task)
admin.site.register(TaskWorkingHours)
