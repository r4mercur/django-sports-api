from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib import admin

from rest_framework.authtoken.models import Token


# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class SportType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sportart"
        verbose_name_plural = "Sportarten"


class GenderType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Geschlecht"
        verbose_name_plural = "Geschlechter"


class Season(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Saison"
        verbose_name_plural = "Saisons"


class Competition(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    gender_type = models.ForeignKey(GenderType, on_delete=models.CASCADE)
    seasons = models.ManyToManyField(Season)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Wettbewerb"
        verbose_name_plural = "Wettbewerbe"


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"


class Match(models.Model):
    team_home = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='home_matches',
        default=None
    )
    team_away = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='away_matches',
        default=None
    )
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True, blank=True)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE, null=True, blank=True)
    match_date = models.DateTimeField("match date")
    match_day = models.IntegerField(null=True, blank=True)
    goals_home = models.IntegerField(null=True, blank=True)
    goals_away = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.team_home} vs {self.team_away}'

    class Meta:
        verbose_name = "Spiel"
        verbose_name_plural = "Spiele"


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100, default=None)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.team is None:
            return self.name
        else:
            return f'{self.name} ({self.team.name})'

    class Meta:
        verbose_name = "Spieler"
        verbose_name_plural = "Spieler"
