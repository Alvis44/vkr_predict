from django.urls import path
from django_filters.views import FilterView

from models import TaskWorkingHours

from . import views

app_name = 'taskBoard'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailEdit.as_view(), name='detail'),
    path('<int:task_id>/Save', views.detail, name='taskSave'),
    path('add', views.TaskCreate.as_view(), name='add'),
    path('CreateTask', views.createTask, name='createTask'),
    path('<int:pk>/Delete', views.TaskDelete.as_view(), name='delete'),
    path('TaskWorkingHours', views.TaskWorkingHoursView.as_view(), name='TaskWorkingHours'),
]