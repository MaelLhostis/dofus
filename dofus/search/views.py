from django.http import HttpResponse
from django.template import loader

from home.models import Player



def index(request):
    template = loader.get_template("search/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def players_all(request):
    template = loader.get_template("search/players.html")
    players = Player.objects.all()
    context = {'players' : players}
    print("1")
    return HttpResponse(template.render(context, request))

def players_level(request, levelMin, levelMax):
    template = loader.get_template("search/players.html")
    players = Player.objects.filter(level__gte=levelMin, level__lte=levelMax)
    context = {'players' : players}
    return HttpResponse(template.render(context, request))

def players_pvpm(request, pvpm):
    template = loader.get_template("search/players.html")
    players = Player.objects.filter(pvpm=pvpm)
    context = {'players' : players}
    return HttpResponse(template.render(context, request))

def players_classe(request, classe):
    template = loader.get_template("search/players.html")
    players = Player.objects.filter(classe=classe)
    context = {'players' : players}
    return HttpResponse(template.render(context, request))


def guilds(request):
    template = loader.get_template("search/guilds.html")
    context = {}
    return HttpResponse(template.render(context, request))

def alliances(request):
    template = loader.get_template("search/alliances.html")
    context = {}
    return HttpResponse(template.render(context, request))