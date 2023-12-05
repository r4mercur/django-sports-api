# here create example data for the application
# using the models defined in competitions/models.py
# and the django ORM
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

# can only be imported after django.setup() need to find a better solution
from django.utils import timezone
from competitions.models import Competition, Team, Player, Match, SportType, GenderType
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

    gt = GenderType(name="Weiblich")
    GenderType(name="Männlich").save()
    gt.save()

    st = SportType(name="Fussball")
    st.save()

    c = Competition(name="Example Competition", gender_type=gt, sport_type=st)
    c.save()

    t1 = Team(name="Team 1", location="München")
    t1.save()
    t2 = Team(name="Team 2", location="Berlin")
    t2.save()

    p1 = Player(name="Player 1", team=t1, position="Torwart", age=randrange(18, 40))
    p1.save()
    p2 = Player(name="Player 2", team=t1, position="Stürmer", age=randrange(18, 40))
    p2.save()
    p3 = Player(name="Player 3", team=t2, position="Verteidiger", age=randrange(18, 40))
    p3.save()
    p4 = Player(name="Player 4", team=t2, position="Mittelfeld", age=randrange(18, 40))
    p4.save()

    # create a match between the two teams
    m = Match(competition=c, team_home=t1, team_away=t2, goals_home=5, goals_away=3, match_date=timezone.now())
    m.save()

    # create a match between the two teams
    m = Match(competition=c, team_home=t2, team_away=t1, goals_home=2, goals_away=3, match_date=timezone.now())
    m.save()

    # create a match between the two teams
    m = Match(competition=c, team_home=t1, team_away=t2, goals_home=3, goals_away=3, match_date=timezone.now())
    m.save()

    # create a match between the two teams
    m = Match(competition=c, team_home=t2, team_away=t1, goals_home=1, goals_away=3, match_date=timezone.now())
    m.save()


if __name__ == '__main__':
    create_example_data()
