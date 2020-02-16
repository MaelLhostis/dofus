from django.db import models
from django import forms

from home.models import DofusClass, Server, Pvpm

class PlayerForm(forms.Form):

    classChoices = [(key.value, key.value) for key in DofusClass]
    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    name = forms.CharField(label='name')
    level = forms.IntegerField(label='level')
    dofusClasse = forms.ChoiceField(choices = classChoices)
    description = forms.CharField(label='description')
    pvpm = forms.ChoiceField(choices = pvpmChoices)
    dbook = forms.CharField(label='dbook')

class GuildForm(forms.Form):

    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    name = forms.CharField(label='name')
    description = forms.CharField(label='description')
    pvpm = forms.ChoiceField(choices = pvpmChoices)
    lvlMinRecrutement = forms.IntegerField(label='lvlMinRecrutement')
    recrutement = forms.BooleanField(label='recrutement')

class AllianceForm(forms.Form):

    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    name = forms.CharField(label='name')
    description = forms.CharField(label='description')
    pvpm = forms.ChoiceField(choices = pvpmChoices)
    lvlMinRecrutement = forms.IntegerField(label='lvlMinRecrutement')
    recrutement = forms.BooleanField(label='recrutement')
