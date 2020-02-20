from django.contrib.auth.models import User
from django.db import models

class CustomMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recever = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = server = models.CharField(max_length=3000)
    date = models.DateField()
