from django.core.management.base import BaseCommand
from django.utils import timezone
from  home.models import Server
from  home.models import Alliance
from  home.models import Guild
from  home.models import Player


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        s = Server()
        s.name = "s1"
        s.save()

        a = Alliance()
        a.server = s 
        a.name = "A1" 
        a.description = "test1"
        a.recrutement = True
        a.lvlMinRecrutement = 59
        a.save()
        
        
        g = Guild()
        g.server = s
        g.alliance = a
        g.name = "g1"
        g.description = "d1"
        g.recrutement = True
        g.lvlMinRecrutement = 80
        g.save()

        p = Player()
        p.server = s
        p.guild = g
        p.name = "p1"
        p.level = 80
        p.classe = "class1"
        p.description = "desc1"
        p.pvpm = "pvp"
        p.dbook = "toto"
        p.save()

        p = Player()
        p.server = s
        p.guild = g
        p.name = "p2"
        p.level = 80
        p.classe = "class2"
        p.description = "desc2"
        p.pvpm = "pvp"
        p.dbook = "toto3"
        p.save()


        p = Player()
        p.server = s
        p.guild = g
        p.name = "p3"
        p.level = 80
        p.classe = "class3"
        p.description = "desc3"
        p.pvpm = "pvp"
        p.dbook = "toto1"
        p.save()