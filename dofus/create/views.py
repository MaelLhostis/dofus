from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from home.models import Player
from .models import PlayerForm

@login_required(login_url='/login')
def index(request):
    template = loader.get_template("create/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def guilds(request):
    template = loader.get_template("create/guilds.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def alliances(request):
    template = loader.get_template("create/alliances.html")
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
    
    context = {'form': form}
    return HttpResponse(template.render(context, request))
