from django.db import models
from django import forms

from home.models import DofusClass, Server, Pvpm

class PlayerForm(forms.Form):

    classDefault = [(None, '------')]
    classQuery = [(key.value, key.value) for key in DofusClass]
    classChoices = classDefault + classQuery
    serverDefault = [(None, '------')]
    serverQuery = [(key.value, key.value) for key in Server]
    serverChoices = serverDefault + serverQuery
    pvpmDefault = [(None, '------')]
    pvpmQuery = [(key.value, key.value) for key in Pvpm]
    pvpmChoices = pvpmDefault + pvpmQuery

    lvlmin = forms.IntegerField(label='lvlmin', required=False)
    lvlmax = forms.IntegerField(label='lvlmax', required=False)
    dofusClass = forms.ChoiceField(choices = classChoices, required=False)
    server = forms.ChoiceField(choices = serverChoices, required=False)
    pvpm = forms.ChoiceField(choices = pvpmChoices, required=False)

class GuildForm(forms.Form):

    serverDefault = [(None, '------')]
    serverQuery = [(key.value, key.value) for key in Server]
    serverChoices = serverDefault + serverQuery
    pvpmDefault = [(None, '------')]
    pvpmQuery = [(key.value, key.value) for key in Pvpm]
    pvpmChoices = pvpmDefault + pvpmQuery

    server = forms.ChoiceField(choices = serverChoices, required=False)
    pvpm = forms.ChoiceField(choices = pvpmChoices, required=False)
    recrutement = forms.BooleanField(required=False)
    lvlmin = forms.IntegerField(label='lvlmin', required=False)

class AllianceForm(forms.Form):

    serverDefault = [(None, '------')]
    serverQuery = [(key.value, key.value) for key in Server]
    serverChoices = serverDefault + serverQuery
    pvpmDefault = [(None, '------')]
    pvpmQuery = [(key.value, key.value) for key in Pvpm]
    pvpmChoices = pvpmDefault + pvpmQuery

    server = forms.ChoiceField(choices = serverChoices, required=False)
    recrutement = forms.BooleanField(required=False)
    lvlmin = forms.IntegerField(label='lvlmin', required=False)