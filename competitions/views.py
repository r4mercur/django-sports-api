from django.shortcuts import render

from django.views import generic
from competitions.models import Competition, SportType


# Create your views here.

class IndexView(generic.ListView):
    template_name = "competitions/index.html"
    context_object_name = "latest_competitions_list"

    def get_queryset(self):
        return Competition.objects.order_by("-pub_date")[:5]
