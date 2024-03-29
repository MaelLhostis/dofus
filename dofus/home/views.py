from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

def index(request):
    template = loader.get_template("home/index.html")
    context = {}
    return HttpResponse(template.render(context, request))