from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("players", views.players, name="players"),
    path("guilds", views.guilds, name="guilds"),
    path("alliances", views.alliances, name="alliances"),
]
