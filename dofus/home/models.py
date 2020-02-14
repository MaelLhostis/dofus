from django.db import models

class User(models.Model):
    mail = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Server(models.Model):
    name = models.CharField(max_length=30)

class Alliance(models.Model):
    idServer = models.ForeignKey(Server, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    descrip = models.CharField(max_length=550)
    recrutement = models.BooleanField()
    lvlMinRecrutement = models.IntegerField()

class Guild(models.Model):
    idServer = models.ForeignKey(Server, on_delete=models.CASCADE)
    idAlliance = models.ForeignKey(Alliance, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    descrip = models.CharField(max_length=550)
    recrutement = models.BooleanField()
    lvlMinRecrutement = models.IntegerField()

class Perso(models.Model):
    idServeur = models.ForeignKey(Server, on_delete=models.CASCADE)
    idGuild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    level = models.IntegerField()
    classe = models.CharField(max_length=15)
    descrip = models.CharField(max_length=550)
    pvpm = models.CharField(max_length=3)
    dbook = models.CharField(max_length=40)



