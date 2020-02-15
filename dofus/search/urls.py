from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_players", views.get_players, name="get_players"),
    path("get_guilds", views.get_guilds, name="get_guilds"),
    path("get_alliances", views.get_alliances, name="get_alliances"),
    path("get_players_user", views.get_players_user, name="get_players_user"),
]
