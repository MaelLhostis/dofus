from django.http import HttpResponse
from django.template import loader
from django import forms
from django.contrib.auth.decorators import login_required

from home.models import Player, Guild, Alliance
from .models import PlayerForm, GuildForm, AllianceForm

@login_required(login_url='/login')
def index(request):
    template = loader.get_template("search/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def get_players(request):

    template = loader.get_template("search/players.html")
    players = Player.objects.all()
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            players = Player.objects.filter(
                level__gte=form.cleaned_data['lvlmin'],
                level__lte=form.cleaned_data['lvlmax'],
                DofusClasse=form.cleaned_data['dofusClass'],
                server=form.cleaned_data['server'],
                pvpm=form.cleaned_data['pvpm'],
                )
    
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
            print(form.cleaned_data)
            players = Player.objects.filter(
                user=request.user,
                level__gte=form.cleaned_data['lvlmin'],
                level__lte=form.cleaned_data['lvlmax'],
                DofusClasse=form.cleaned_data['dofusClass'],
                server=form.cleaned_data['server'],
                pvpm=form.cleaned_data['pvpm'],
                )
    
    context = {'form': form, 'players' : players}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def get_guilds(request):

    template = loader.get_template("search/guilds.html")
    guilds = Guild.objects.all()
    form = GuildForm()
    if request.method == 'POST':
        form = GuildForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            guilds = Guild.objects.filter(
                lvlMinRecrutement__gte=form.cleaned_data['lvlmin'],
                server=form.cleaned_data['server'],
                pvpm=form.cleaned_data['pvpm'],
                recrutement=form.cleaned_data['recrutement'] 
                )

    context = {'form': form, 'guilds' : guilds}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def get_alliances(request):

    template = loader.get_template("search/alliances.html")
    alliances = Alliance.objects.all()
    form = AllianceForm()
    if request.method == 'POST':
        form = AllianceForm(request.POST)
        if form.is_valid():   
            print(form.cleaned_data)
            alliances = Alliance.objects.filter(
                lvlMinRecrutement__gte=form.cleaned_data['lvlmin'],
                server=form.cleaned_data['server'],
                recrutement=form.cleaned_data['recrutement']
                )
    
    context = {'form': form, 'alliances' : alliances}
    return HttpResponse(template.render(context, request))
