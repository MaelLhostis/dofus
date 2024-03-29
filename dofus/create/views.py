from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from home.models import Player, Guild, Alliance
from .models import PlayerForm, GuildForm, AllianceForm

@login_required(login_url='/login')
def index(request):
    template = loader.get_template("create/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def players(request):
    template = loader.get_template("create/players.html")
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            p = Player()
            p.user = request.user
            p.server = form.cleaned_data['server']
            p.name = form.cleaned_data['name']
            p.level = form.cleaned_data['level']
            p.DofusClasse = form.cleaned_data['dofusClasse']
            p.description = form.cleaned_data['description']
            p.pvpm = form.cleaned_data['pvpm']
            p.dbook = form.cleaned_data['dbook']
            p.save()
            return redirect('/search/get_players')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def guilds(request):
    template = loader.get_template("create/guilds.html")
    form = GuildForm()
    if request.method == 'POST':
        form = GuildForm(request.POST)
        if form.is_valid():
            p = Guild()
            p.user = request.user
            p.server = form.cleaned_data['server']
            p.name = form.cleaned_data['name']
            p.description = form.cleaned_data['description']
            p.pvpm = form.cleaned_data['pvpm']
            p.recrutement = form.cleaned_data['recrutement']
            p.lvlMinRecrutement = form.cleaned_data['lvlMinRecrutement']
            p.save()
            return redirect('/search/get_guilds')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def alliances(request):
    template = loader.get_template("create/alliances.html")
    form = AllianceForm()
    if request.method == 'POST':
        form = AllianceForm(request.POST)
        if form.is_valid():
            p = Alliance()
            p.user = request.user
            p.server = form.cleaned_data['server']
            p.name = form.cleaned_data['name']
            p.description = form.cleaned_data['description']
            p.recrutement = form.cleaned_data['recrutement']
            p.lvlMinRecrutement = form.cleaned_data['lvlMinRecrutement']
            p.save()
            return redirect('/search/get_alliances')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
