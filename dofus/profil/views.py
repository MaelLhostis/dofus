from django.http import HttpResponse
from django.template import loader

from home.models import Player, Guild, Alliance

def index(request):
    template = loader.get_template("profil/index.html")
    players = Player.objects.filter(user = request.user)
    guilds = Guild.objects.filter(user = request.user)
    alliances = Alliance.objects.filter(user = request.user)
    context = {"players": players, "guilds": guilds, "alliances": alliances}
    return HttpResponse(template.render(context, request))
