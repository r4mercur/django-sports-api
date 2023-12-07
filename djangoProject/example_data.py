# here create example data for the application
# using the models defined in competitions/models.py
# and the django ORM
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

# can only be imported after django.setup() need to find a better solution
from django.utils import timezone
from competitions.models import Competition, Team, Player, Match, SportType, GenderType, Season
from random import randrange


def data_already_exists():
    if Competition.objects.all().count() > 0:
        return True
    else:
        return False


def create_example_data():
    if data_already_exists():
        print("Example data already exists \n")
        return

    gt = GenderType(name="Männlich")
    GenderType(name="Weiblich").save()
    gt.save()

    st = SportType(name="Fussball")
    st.save()

    i = 1
    while i < 11:
        s = Season(name="Saison " + str(i), start_date=timezone.now(), end_date=timezone.now())
        s.save()
        i += 1

    s1 = Season.objects.get(pk=10)
    c = Competition(name="1. Bundesliga", gender_type=gt, sport_type=st)
    c.save()
    c.seasons.add(s1)
    c.save()

    i = 1
    while i < 19:
        t = Team(name="Team " + str(i), location="Location " + str(i))
        t.save()

        # create players
        for x in range(0, 18):
            position = ""
            if x < 9 and x % 2 == 0:
                position = "Verteidiger"
            elif x < 9 and x % 2 != 0:
                position = "Stürmer"
            elif x >= 9 and x % 2 == 0:
                position = "Torwart"
            p = Player(name="Player " + str(x), team=Team.objects.get(pk=i), position=position, age=randrange(18, 35))
            p.save()
        i += 1

    i = 1
    while i < 257:
        match = Match(team_home=Team.objects.get(pk=randrange(1, 18)),
                      team_away=Team.objects.get(pk=randrange(1, 18)),
                      goals_home=randrange(0, 6),
                      goals_away=randrange(0, 6),
                      match_day=i,
                      competition=c,
                      sport_type=st,
                      match_date=timezone.now())
        match.save()
        i += 1


if __name__ == '__main__':
    create_example_data()
