# Generated by Django 4.2.7 on 2023-11-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_team_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='goals_away',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='match',
            name='goals_home',
            field=models.IntegerField(default=None),
        ),
    ]
