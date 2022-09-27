from dataclasses import field
from django.forms import ModelForm, HiddenInput
from todolist.models import Task

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', ]