from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("players", views.players_all, name="players_all"),
    path("players/<int:levelMin>/<int:levelMax>", views.players_level, name="players_level"),
    path("players/<str:pvpm>", views.players_pvpm, name="players_pvpm"),
    path("guilds", views.guilds, name="guilds"),
    path("alliances", views.alliances, name="alliances"),
]
