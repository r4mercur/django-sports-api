from django.test import TestCase
from .models import SportType, GenderType, Competition, Team, Match, Player

# Create your tests here.
class SportTypeTestCase(TestCase):
    def setUp(self):
        SportType.objects.create(name="Football")
        SportType.objects.create(name="Basketball")

    def test_sport_type_name(self):
        football = SportType.objects.get(name="Football")
        basketball = SportType.objects.get(name="Basketball")
        self.assertEqual(football.name, "Football")
        self.assertEqual(basketball.name, "Basketball")

class GenderTypeTestCase(TestCase):
    def setUp(self):
        GenderType.objects.create(name="Weiblich")
        GenderType.objects.create(name="Männlich")
        GenderType.objects.create(name="Divers")

    def test_gender_type_name(self):
        woman = GenderType.objects.get(name="Weiblich")
        man = GenderType.objects.get(name="Männlich")
        n_binary = GenderType.objects.get(name="Divers")
        self.assertEqual(woman.name, "Weiblich")
        self.assertEqual(man.name, "Männlich")
        self.assertEqual(n_binary.name, "Divers")


class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="FC Bayern München", location="München")
        Team.objects.create(name="FC Barcelona", location="Barcelona")

    def test_team_name(self):
        bayern = Team.objects.get(name="FC Bayern München")
        barcelona = Team.objects.get(name="FC Barcelona")
        self.assertEqual(bayern.name, "FC Bayern München")
        self.assertEqual(barcelona.name, "FC Barcelona")

    def test_team_location(self):
        bayern = Team.objects.get(name="FC Bayern München")
        barcelona = Team.objects.get(name="FC Barcelona")
        self.assertEqual(bayern.location, "München")
        self.assertEqual(barcelona.location, "Barcelona")


class CompetitionTestCase(TestCase):
    def setUp(self):
        st = SportType.objects.create(name="Football")
        gt = GenderType.objects.create(name="Weiblich")
        Competition.objects.create(name="1. Bundesliga", sport_type=st, gender_type=gt)

    def test_competition_name(self):
        bundesliga = Competition.objects.get(name="1. Bundesliga")
        self.assertEqual(bundesliga.name, "1. Bundesliga")


class MatchTestCase(TestCase):
    def setUp(self):
        st = SportType.objects.create(name="Football")
        gt = GenderType.objects.create(name="Weiblich")
        comp = Competition.objects.create(name="1. Bundesliga", sport_type=st, gender_type=gt)
        bayern = Team.objects.create(name="FC Bayern München", location="München")
        barcelona = Team.objects.create(name="FC Barcelona", location="Barcelona")
        Match.objects.create(
            team_home=bayern,
            team_away=barcelona,
            competition=comp,
            sport_type=st,
            match_date="2021-10-01 20:00",
            goals_home=2,
            goals_away=1,
        )

    def test_match_team_home(self):
        bayern = Team.objects.get(name="FC Bayern München")
        match = Match.objects.get(team_home=bayern)
        self.assertEqual(match.team_home.name, "FC Bayern München")

class PlayerTestCase(TestCase):
    def setUp(self):
        Player.objects.create(name="Lionel Messi", age=34, position="Stürmer")
        Player.objects.create(name="Robert Lewandowski", age=33, position="Stürmer")
    
    def test_player_name(self):
        messi = Player.objects.get(name="Lionel Messi")
        lewa = Player.objects.get(name="Robert Lewandowski")
        self.assertEqual(messi.name, "Lionel Messi")
        self.assertEqual(lewa.name, "Robert Lewandowski")