from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ("username",)
        field_classes = {'username': UsernameField}

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
            'email'
        )


class LeadModelform(forms.ModelForm):
    class Meta:
        model = Leads
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields= (
            'first_name',
            'last_name',
            'user'
        )
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = (
            'first_name',
            'last_name',
            'age'
        )

class Leadform(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CreateAgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'first_name',
            'last_name',
            'user'
        )
