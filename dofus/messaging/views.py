from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User

from .models import Messaging, MessagingForm

def index(request):
    template = loader.get_template("messaging/index.html")
    form = MessagingForm()
    if request.method == 'POST':
        form = MessagingForm(request.POST)
        if form.is_valid():
            m = Messaging()
            m.sender = request.user
            m.recever = User.objects.get(username=form.cleaned_data['users'])
            m.message_text = form.cleaned_data['message']
            m.save()
    context = {'form': form}
    return HttpResponse(template.render(context, request))

