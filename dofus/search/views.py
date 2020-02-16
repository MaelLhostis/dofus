from django.http import HttpResponse
from django.template import loader
from django import forms
from django.contrib.auth.decorators import login_required

from home.models import Player, Guild, Alliance
from .models import PlayerForm, GuildForm, AllianceForm

def index(request):
    template = loader.get_template("search/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def get_players(request):
    template = loader.get_template("search/players.html")
    players = Player.objects.all()
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            players = Player.objects.all()
            if form.cleaned_data['lvlmin'] is not None:
                players = players.filter(level__gte=form.cleaned_data['lvlmin'])
            if form.cleaned_data['lvlmax'] is not None:
                players = players.filter(level__level__ltegte=form.cleaned_data['lvlmax'])
            if form.cleaned_data['dofusClass'] is not None and form.cleaned_data['dofusClass'] is not "":
                players = players.filter(DofusClasse=form.cleaned_data['dofusClass'])
            if form.cleaned_data['server'] is not None and form.cleaned_data['server'] is not "":
                players = players.filter(server=form.cleaned_data['server'])
            if form.cleaned_data['pvpm'] is not None and form.cleaned_data['pvpm'] is not "":
                players = players.filter(pvpm=form.cleaned_data['pvpm'])
    context = {'form': form, 'players' : players}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def get_players_user(request):

    template = loader.get_template("search/players.html")
    players = Player.objects.filter(user=request.user)
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            players = Player.objects.all()
            players = players.filter(user=request.user)
            if form.cleaned_data['lvlmin'] is not None:
                players = players.filter(level__gte=form.cleaned_data['lvlmin'])
            if form.cleaned_data['lvlmax'] is not None:
                players = players.filter(level__level__ltegte=form.cleaned_data['lvlmax'])
            if form.cleaned_data['dofusClass'] is not None and form.cleaned_data['dofusClass'] is not "":
                players = players.filter(DofusClasse=form.cleaned_data['dofusClass'])
            if form.cleaned_data['server'] is not None and form.cleaned_data['server'] is not "":
                players = players.filter(server=form.cleaned_data['server'])
            if form.cleaned_data['pvpm'] is not None and form.cleaned_data['pvpm'] is not "":
                players = players.filter(pvpm=form.cleaned_data['pvpm'])
    context = {'form': form, 'players' : players}
    return HttpResponse(template.render(context, request))

def get_guilds(request):

    template = loader.get_template("search/guilds.html")
    guilds = Guild.objects.all()
    form = GuildForm()
    if request.method == 'POST':
        form = GuildForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            guilds = Guild.objects.all()
            if form.cleaned_data['lvlmin'] is not None:
                guilds = guilds.filter(lvlMinRecrutement__gte=form.cleaned_data['lvlmin'])
            if form.cleaned_data['server'] is not None and form.cleaned_data['server'] is not "":
                guilds = guilds.filter(server=form.cleaned_data['server'])
            if form.cleaned_data['pvpm'] is not None and form.cleaned_data['pvpm'] is not "":
                guilds = guilds.filter(pvpm=form.cleaned_data['pvpm'])
            guilds = guilds.filter(recrutement=form.cleaned_data['recrutement'])
    context = {'form': form, 'guilds' : guilds}
    return HttpResponse(template.render(context, request))

def get_alliances(request):

    template = loader.get_template("search/alliances.html")
    alliances = Alliance.objects.all()
    form = AllianceForm()
    if request.method == 'POST':
        form = AllianceForm(request.POST)
        if form.is_valid():
            alliances = Alliance.objects.all()
            if form.cleaned_data['lvlmin'] is not None:
                alliances = alliances.filter(lvlMinRecrutement__gte=form.cleaned_data['lvlmin'])
            if form.cleaned_data['server'] is not None and form.cleaned_data['server'] is not "":
                alliances = alliances.filter(server=form.cleaned_data['server'])
            alliances = alliances.filter(recrutement=form.cleaned_data['recrutement'])
    
    context = {'form': form, 'alliances' : alliances}
    return HttpResponse(template.render(context, request))
