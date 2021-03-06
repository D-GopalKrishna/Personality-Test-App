from django import forms
from django.db import models
from django.forms import ModelForm, fields
from .models import UserData, UserChoice, userSelection

class UserDataForm(forms.ModelForm):
    class Meta:    
        model = UserData
        fields = '__all__'


class UserChoiceForm(forms.ModelForm):
    class Meta:
        model = UserChoice
        fields = '__all__'


class userSelectionForm(forms.ModelForm):
    class Meta:
        model = userSelection
        fields = '__all__'