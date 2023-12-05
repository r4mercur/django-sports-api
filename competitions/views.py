import json

from django.http import HttpResponse
from django.views import generic
from rest_framework import generics

from competitions.models import Competition, SportType, GenderType, Match, Team
from .serializers import CompetitionSerializer, SportTypeSerializer, TeamSerializer, GenderTypeSerializer, \
    MatchSerializer


# Create your views here.
def calculate_table(request, pk):
    competition = Competition.objects.get(pk=pk)
    teams = Team.objects.all()
    matches = Match.objects.filter(competition=competition)
    table = []
    for team in teams:
        points = 0
        goals = 0
        goals_conceded = 0
        wins = 0
        draws = 0
        losses = 0
        for match in matches:
            if match.team_home == team:
                goals += match.goals_home
                goals_conceded += match.goals_away
                if match.goals_home > match.goals_away:
                    points += 3
                    wins += 1
                elif match.goals_home == match.goals_away:
                    points += 1
                    draws += 1
                else:
                    losses += 1
            elif match.team_away == team:
                goals += match.goals_away
                goals_conceded += match.goals_home
                if match.goals_away > match.goals_home:
                    points += 3
                    wins += 1
                elif match.goals_away == match.goals_home:
                    points += 1
                    draws += 1
                else:
                    losses += 1
        table.append({
            "team": team.name,
            "points": points,
            "goals": goals,
            "goals_conceded": goals_conceded,
            "wins": wins,
            "draws": draws,
            "losses": losses
        })
    table.sort(key=lambda x: x["points"], reverse=True)
    return HttpResponse(json.dumps(table), content_type="application/json")


# API views
class APICompetitionView(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class APISportTypeView(generics.ListCreateAPIView):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer


class APIGenderTypeView(generics.ListCreateAPIView):
    queryset = GenderType.objects.all()
    serializer_class = GenderTypeSerializer


class APIMatchView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class APITeamView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# Other views

class IndexView(generic.ListView):
    template_name = "competitions/index.html"
    context_object_name = "latest_competitions_list"

    def get_queryset(self):
        return Competition.objects.order_by("-id")[:5]
