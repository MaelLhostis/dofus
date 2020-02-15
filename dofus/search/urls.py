from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("players", views.players_all, name="players_all"),
    path("get_players", views.get_players, name="get_players"),
    path("guilds", views.guilds, name="guilds"),
    path("alliances", views.alliances, name="alliances"),
]
