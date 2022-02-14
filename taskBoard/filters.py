import django_filters
from .models import TaskWorkingHours

class TaskWorkingHoursFilter(django_filters.FilterSet):
    class Meta:
        model = TaskWorkingHours
        fields = ['taskInWork']