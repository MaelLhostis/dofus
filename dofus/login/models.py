from django.db import models
from django import forms


class ConnectForm(forms.Form):

    username = forms.CharField(label='username')
    password = forms.CharField(label='password')

class SubscribeForm(forms.Form):

    mail = forms.CharField(label='mail')
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')