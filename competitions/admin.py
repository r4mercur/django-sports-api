from django.contrib import admin

from .models import Competition, GenderType, SportType, Team, Match

# Register your models here.
admin.site.register(SportType)
admin.site.register(GenderType)
admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Match)
