from django.db import models
from django import forms


class ConnectForm(forms.Form):

    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'Entrez un username'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Entrez un password'}))
class SubscribeForm(forms.Form):

    mail = forms.CharField(label='mail', widget=forms.TextInput(attrs={'placeholder': 'Entrez un Email'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'Entrez un username'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Entrez un password'}))