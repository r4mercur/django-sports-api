from django.contrib import admin

from .models import Competition, GenderType, SportType, Team, Match, Player


class MatchAdmin(admin.ModelAdmin):
    list_display = ('team_home', 'team_away', 'goals_home', 'goals_away', 'match_day', 'competition', 'sport_type',
                    'match_date')
    ordering = ('match_day', 'match_date')
    list_filter = ('competition', 'sport_type', 'match_date')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'position', 'age')
    ordering = ('name', 'team', 'position', 'age')
    list_filter = ('team', 'position', 'age')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    ordering = ('name', 'location')
    list_filter = ('name', 'location')


# Register your models here.
admin.site.register(SportType)
admin.site.register(GenderType)
admin.site.register(Competition)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Player, PlayerAdmin)
