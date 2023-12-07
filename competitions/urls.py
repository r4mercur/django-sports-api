from django.urls import path

from . import views
from .views import APICompetitionView, APISportTypeView, APIGenderTypeView, APIMatchView, APITeamView

app_name = "competitions"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),

    # general
    path("api/seasons/", views.APISeasonView.as_view(), name="api_seasons"),
    path("api/competitions/", APICompetitionView.as_view(), name="api_competitions"),
    path("api/sport_types/", APISportTypeView.as_view(), name="api_sport_types"),
    path("api/gender_types/", APIGenderTypeView.as_view(), name="api_gender_types"),

    # matches
    path("api/matches/", APIMatchView.as_view(), name="api_matches"),
    path("api/matches/<int:competition_id>/", views.APICompetitionMatches.as_view(), name="competition_matches"),

    # teams
    path("api/teams/", APITeamView.as_view(), name="api_teams"),
    path("api/players/", views.APIPlayerView.as_view(), name="api_players"),

    # other views
    path("api/competitions/table/<int:pk>/", views.calculate_table, name="calctable_competition"),
]
