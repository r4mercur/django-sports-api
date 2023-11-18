from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

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


class GenderType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    gender_type = models.ForeignKey(GenderType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


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
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE, null=True, blank=True)
    goals_home = models.IntegerField(null=True, blank=True)
    goals_away = models.IntegerField(null=True, blank=True)
