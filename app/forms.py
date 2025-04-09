from django import forms
from app.models import *

class TaskForms(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'