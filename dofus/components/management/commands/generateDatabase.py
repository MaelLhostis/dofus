from django.core.management.base import BaseCommand
from django.utils import timezone
from  home.models import Server
from  home.models import Alliance
from  home.models import Guild
from  home.models import Player
from  home.models import DofusClass
from  home.models import Pvpm

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        a = Alliance()
        a.server = Server.JULITH
        a.name = "A1" 
        a.description = "test1"
        a.recrutement = True
        a.lvlMinRecrutement = 59
        a.save()
        
        
        g = Guild()
        g.server = Server.PANDORE
        g.alliance = a
        g.name = "g1"
        g.description = "d1"
        g.recrutement = True
        g.lvlMinRecrutement = 80
        g.pvpm = Pvpm.PVM
        g.save()

        p = Player()
        p.server = Server.ILYZAELLE
        p.guild = g
        p.name = "p1"
        p.level = 80
        p.classe = DofusClass.FECA
        p.description = "desc1"
        p.pvpm = Pvpm.PVM
        p.dbook = "toto"
        p.save()

        p = Player()
        p.server = Server.AGRIDE
        p.guild = g
        p.name = "p2"
        p.level = 160
        p.classe = DofusClass.ZOBAL
        p.description = "desc2"
        p.pvpm = Pvpm.PVP
        p.dbook = "toto3"
        p.save()


        p = Player()
        p.server = Server.AGRIDE
        p.guild = g
        p.name = "p3"
        p.level = 40
        p.classe = DofusClass.ENUTROF
        p.description = "desc3"
        p.pvpm = Pvpm.PVM
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.OMBRE
        p.guild = g
        p.name = "p3"
        p.level = 200
        p.classe = DofusClass.FECA
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM
        p.dbook = "toto1"
        p.save()


        p = Player()
        p.server = Server.OMBRE
        p.guild = g
        p.name = "p3"
        p.level = 120
        p.classe = DofusClass.SACRIEUR
        p.description = "desc3"
        p.pvpm = Pvpm.PVM
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.BRUMEN
        p.guild = g
        p.name = "p3"
        p.level = 40
        p.classe = DofusClass.HUPPERMAGE
        p.description = "desc3"
        p.pvpm = Pvpm.PVP
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH
        p.guild = g
        p.name = "p3"
        p.level = 186
        p.classe = DofusClass.XELOR
        p.description = "desc3"
        p.pvpm = Pvpm.PVP
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.NIDAS
        p.guild = g
        p.name = "p3"
        p.level = 186
        p.classe = DofusClass.SADIDA
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH
        p.guild = g
        p.name = "p3"
        p.level = 186
        p.classe = DofusClass.XELOR
        p.description = "desc3"
        p.pvpm = Pvpm.PVP
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.classe = DofusClass.XELOR
        p.description = "desc3"
        p.pvpm = Pvpm.PVP
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.classe = DofusClass.ZOBAL
        p.description = "desc3"
        p.pvpm = Pvpm.PVM
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.OMBRE
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.classe = DofusClass.OUGINAK
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.MERKATOR
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.classe = DofusClass.ZOBAL
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM
        p.dbook = "toto1"
        p.save()