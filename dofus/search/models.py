from django.db import models
from django import forms

from home.models import DofusClass, Server, Pvpm

class PlayerForm(forms.Form):

    classChoices = [(key.value, key.value) for key in DofusClass]
    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    lvlmin = forms.IntegerField(label='lvlmin')
    lvlmax = forms.IntegerField(label='lvlmax')
    dofusClass = forms.ChoiceField(choices = classChoices)
    server = forms.ChoiceField(choices = serverChoices)
    pvpm = forms.ChoiceField(choices = pvpmChoices)

class GuildForm(forms.Form):

    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    pvpm = forms.ChoiceField(choices = pvpmChoices)
    recrutement = forms.BooleanField()
    lvlmin = forms.IntegerField(label='lvlmin')

class AllianceForm(forms.Form):

    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    recrutement = forms.BooleanField()
    lvlmin = forms.IntegerField(label='lvlmin')