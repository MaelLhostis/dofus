from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import ConnectForm, SubscribeForm

def log_in(request):
    template = loader.get_template("login/login.html")
    form = ConnectForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ConnectForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                )
            if user is not None:
                    login(request, user)
                    request.session['user_id'] = user.id
                    return redirect('/home')
            else:
                context['error'] = 'Mauvais login / password'
    print(context)
    return HttpResponse(template.render(context, request))

def log_out(request):
    logout(request)
    return redirect('/login')

def subscribe(request):
    template = loader.get_template("login/subscribe.html")
    form = SubscribeForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            u = User()
            u.email = form.cleaned_data['mail']
            u.username = form.cleaned_data['username']
            u.set_password(form.cleaned_data['password'])
            u.save()
            return redirect('/login')
    return HttpResponse(template.render(context, request))