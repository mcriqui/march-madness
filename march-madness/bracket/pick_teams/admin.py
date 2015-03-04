from django.contrib import admin
from pick_teams.models import Ranking


class RankingAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'mascot_name')

admin.site.register(Ranking, RankingAdmin)
