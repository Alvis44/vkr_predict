from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import default

from .models import Task


class TaskCreateForm(forms.Form):

    LIST_VALUE = Task.LIST_VALUE.copy()
    LIST_VALUE.insert(0, ('', ''))
    title = forms.CharField(required=False)
    status = forms.ChoiceField(choices=LIST_VALUE, required=False)
    create_by = forms.ModelChoiceField(User.objects.all(), required=False)

