from django.http import HttpResponse
from django.template import loader

from home.models import Player, Guild, Alliance
from messaging.models import Messaging

def index(request):
    template = loader.get_template("profil/index.html")
    players = Player.objects.filter(user = request.user)
    guilds = Guild.objects.filter(user = request.user)
    alliances = Alliance.objects.filter(user = request.user)
    messages_send = Messaging.objects.filter(sender = request.user)
    messages_receved = Messaging.objects.filter(recever = request.user)
    context = {"players": players, "guilds": guilds, "alliances": alliances, "messages_send": messages_send, "messages_receved": messages_receved}
    return HttpResponse(template.render(context, request))
