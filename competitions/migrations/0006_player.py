# Generated by Django 4.2.7 on 2023-12-05 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0005_match_sport_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('position', models.CharField(default=None, max_length=100)),
                ('team', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='competitions.team')),
            ],
        ),
    ]
