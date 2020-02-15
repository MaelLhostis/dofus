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
        a.server = Server.JULITH.value
        a.name = "A1" 
        a.description = "test1"
        a.recrutement = True
        a.lvlMinRecrutement = 59
        a.save()
        
        
        g = Guild()
        g.server = Server.PANDORE.value
        g.alliance = a
        g.name = "g1"
        g.description = "d1"
        g.recrutement = True
        g.lvlMinRecrutement = 80
        g.pvpm = Pvpm.PVM.value
        g.save()

        p = Player()
        p.server = Server.ILYZAELLE.value
        p.guild = g
        p.name = "p1"
        p.level = 80
        p.DofusClasse = DofusClass.FECA.value
        p.description = "desc1"
        p.pvpm = Pvpm.PVP.value
        p.dbook = "toto"
        p.save()

        p = Player()
        p.server = Server.AGRIDE.value
        p.guild = g
        p.name = "p2"
        p.level = 160
        p.DofusClasse = DofusClass.ZOBAL.value
        p.description = "desc2"
        p.pvpm = Pvpm.PVP.value
        p.dbook = "toto3"
        p.save()


        p = Player()
        p.server = Server.AGRIDE.value
        p.guild = g
        p.name = "p3"
        p.level = 40
        p.DofusClasse = DofusClass.ENUTROF.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVM.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.OMBRE.value
        p.guild = g
        p.name = "p3"
        p.level = 200
        p.DofusClasse = DofusClass.FECA.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM.value
        p.dbook = "toto1"
        p.save()


        p = Player()
        p.server = Server.OMBRE.value
        p.guild = g
        p.name = "p3"
        p.level = 120
        p.DofusClasse = DofusClass.SACRIEUR.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVM.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.BRUMEN.value
        p.guild = g
        p.name = "p3"
        p.level = 40
        p.DofusClasse = DofusClass.HUPPERMAGE.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVP.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH.value
        p.guild = g
        p.name = "p3"
        p.level = 186
        p.DofusClasse = DofusClass.XELOR.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVP.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.NIDAS.value
        p.guild = g
        p.name = "p3"
        p.level = 186
        p.DofusClasse = DofusClass.SADIDA.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH.value
        p.guild = g
        p.name = "p3"
        p.level = 186
        p.DofusClasse = DofusClass.XELOR.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVP.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH.value
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.DofusClasse = DofusClass.XELOR.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVP.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.JULITH.value
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.DofusClasse = DofusClass.ZOBAL.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVM.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.OMBRE.value
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.DofusClasse = DofusClass.OUGINAK.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM.value
        p.dbook = "toto1"
        p.save()

        p = Player()
        p.server = Server.MERKATOR.value
        p.guild = g
        p.name = "p3"
        p.level = 75
        p.DofusClasse = DofusClass.ZOBAL.value
        p.description = "desc3"
        p.pvpm = Pvpm.PVPM.value
        p.dbook = "toto1"
        p.save()