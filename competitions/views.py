from django.shortcuts import render

from django.views import generic
from competitions.models import Competition, SportType, GenderType, Match, Team
from rest_framework import generics
from .serializers import CompetitionSerializer, SportTypeSerializer, TeamSerializer, GenderTypeSerializer, \
    MatchSerializer


# Create your views here.

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
        return Competition.objects.order_by("-pub_date")[:5]
