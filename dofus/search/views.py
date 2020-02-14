from django.http import HttpResponse
from django.template import loader



def index(request):
    template = loader.get_template("search/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def players(request):
    template = loader.get_template("search/players.html")
    context = {'array' : [1,2,3,4,5,6]}
    return HttpResponse(template.render(context, request))

def guilds(request):
    template = loader.get_template("search/guilds.html")
    context = {}
    return HttpResponse(template.render(context, request))

def alliances(request):
    template = loader.get_template("search/alliances.html")
    context = {}
    return HttpResponse(template.render(context, request))