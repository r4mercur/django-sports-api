# Generated by Django 4.2.7 on 2023-11-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_alter_match_goals_away_alter_match_goals_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='goals_away',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='goals_home',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
