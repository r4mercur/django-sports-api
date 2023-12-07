from rest_framework import serializers
from .models import Competition, SportType, GenderType, Match, Team, Player, Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'


class GenderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderType
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
