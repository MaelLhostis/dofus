from django.db import models
from django import forms

class PlayerForm(forms.Form):

    lvlmin = forms.IntegerField(label='lvlmin')
    lvlmax = forms.IntegerField(label='lvlmax')