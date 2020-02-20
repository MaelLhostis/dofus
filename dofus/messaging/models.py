from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import Q

class Messaging(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    recever = models.ForeignKey(User, related_name='recever', on_delete=models.CASCADE)
    message_text = models.CharField(max_length=2550)

class MessagingForm(forms.Form):
    users = User.objects.all()
    message = forms.CharField(max_length=2550)
    usersChoices = [(user.username, user.username) for user in users]
    users = forms.ChoiceField(choices = usersChoices)