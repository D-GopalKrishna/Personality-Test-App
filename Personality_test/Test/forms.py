from django import forms
from django.db import models
from django.forms import ModelForm, fields
from .models import UserName, UserChoice

class UserNameForm(forms.ModelForm):
    class Meta:    
        model = UserName
        fields = '__all__'


class UserChoiceForm(forms.ModelForm):
    class Meta:
        model = UserChoice
        fields = '__all__'