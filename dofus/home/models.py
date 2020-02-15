from django.contrib.auth.models import User
from django.db import models
import enum

class Server(enum.Enum):
    AGRIDE = "Agride"
    ILYZAELLE = "Illyzaelle"
    USH = "Ush"
    MERIANA = "Mériana"
    PANDORE = "Pandore"
    NIDAS = "Nidas"
    MERKATOR = "Merkator"
    BRUMEN = "Brumen"
    JULITH = "Julith"
    FURYE = "Furye"
    OTOMUSTAN = "Oto Mustam"
    OMBRE = "Ombre"

class DofusClass(enum.Enum):
    CRA = "Cra"
    ECAFLIP = "Ecaflip"
    ENIRIPSA = "Eniripsa"
    IOP = "Iop"
    FECA = "Féca"
    SACRIEUR = "Sacrieur"
    SADIDA = "Sadida"
    OSAMODAS = "Osamodas"
    ENUTROF = "Enutrof"
    SRAM = "Sram"
    XELOR = "Xelor"
    PANDAWA = "Pandawa"
    ROUBLARD ="Roublard"
    ZOBAL = "Zobal"
    STEAMER = "Steamer"
    ELIOTROPE = "Eliotrope"
    HUPPERMAGE = "Hupermage"
    OUGINAK = "Ouginak"

class Pvpm(enum.Enum):
    PVP = "PVP"
    PVM = "PVM"
    PVPM = "PVP/PVM"

class Alliance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=550)
    recrutement = models.BooleanField()
    lvlMinRecrutement = models.IntegerField()

class Guild(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server =  models.CharField(max_length=250)
    alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=550)
    recrutement = models.BooleanField()
    lvlMinRecrutement = models.IntegerField()
    pvpm = models.CharField(max_length=50)

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server =  models.CharField(max_length=250)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    level = models.IntegerField()
    DofusClasse = models.CharField(max_length=250)
    description = models.CharField(max_length=550)
    pvpm = models.CharField(max_length=250)
    dbook = models.CharField(max_length=250)

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    articleContent = models.CharField(max_length=1000)
    articleDate = models.DateField()
    