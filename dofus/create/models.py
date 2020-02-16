from django.db import models
from django import forms

from home.models import DofusClass, Server, Pvpm

class PlayerForm(forms.Form):

    classChoices = [(key.value, key.value) for key in DofusClass]
    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Entrez votre nom'}))
    level = forms.IntegerField(label='level', widget=forms.TextInput(attrs={'placeholder': 'Entrez votre level'}), max_value=200)
    dofusClasse = forms.ChoiceField(choices = classChoices, initial="default")
    description = forms.CharField(label='description', widget=forms.TextInput(attrs={'placeholder': 'Entrez une description'}), max_length=550)
    pvpm = forms.ChoiceField(choices = pvpmChoices)
    dbook = forms.CharField(label='dbook', widget=forms.TextInput(attrs={'placeholder': 'Entrez votre lien dbook'}))

class GuildForm(forms.Form):

    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Entrez un nom'}))
    description = forms.CharField(label='description', widget=forms.TextInput(attrs={'placeholder': 'Entrez une description'}), max_length=550)
    pvpm = forms.ChoiceField(choices = pvpmChoices)
    lvlMinRecrutement = forms.IntegerField(label='Level min de recrutement', widget=forms.TextInput(attrs={'placeholder': 'Entrez le level de recrutement'}), max_value=200)
    recrutement = forms.BooleanField(label='recrutement', required=False)

class AllianceForm(forms.Form):

    serverChoices = [(key.value, key.value) for key in Server]
    pvpmChoices = [(key.value, key.value) for key in Pvpm]

    server = forms.ChoiceField(choices = serverChoices)
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Entrez un nom'}))
    description = forms.CharField(label='description', widget=forms.TextInput(attrs={'placeholder': 'Entrez une description'}), max_length=550)
    pvpm = forms.ChoiceField(choices = pvpmChoices)
    lvlMinRecrutement = forms.IntegerField(label='Level min de recrutement', widget=forms.TextInput(attrs={'placeholder': 'Entrez le level de recrutement'}), max_value=200)
    recrutement = forms.BooleanField(label='recrutement', required=False)
