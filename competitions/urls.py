from django.urls import path

from . import views
from .views import APICompetitionView, APISportTypeView, APIGenderTypeView, APIMatchView, APITeamView

app_name = "competitions"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api/competitions/", APICompetitionView.as_view(), name="api_competitions"),
    path("api/sport_types/", APISportTypeView.as_view(), name="api_sport_types"),
    path("api/gender_types/", APIGenderTypeView.as_view(), name="api_gender_types"),
    path("api/matches/", APIMatchView.as_view(), name="api_matches"),
    path("api/teams/", APITeamView.as_view(), name="api_teams"),
]
