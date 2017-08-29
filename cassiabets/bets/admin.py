# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from bets import models

# =============================================================================
# Apostador
# =============================================================================
class PlayerAdmin(admin.ModelAdmin):

    list_display = ('name', 'cash', 'points')

admin.site.register(models.Player, PlayerAdmin)

# =============================================================================
# Time
# =============================================================================
class TeamAdmin(admin.ModelAdmin):

    list_display = ('name', )

admin.site.register(models.Team, TeamAdmin)

# =============================================================================
# Partida
# =============================================================================
class MatchAdmin(admin.ModelAdmin):

    list_display = ('team_1', 'team_2', 'winner', 'tie')

admin.site.register(models.Match, MatchAdmin)

# =============================================================================
# Aposta
# =============================================================================
class BetAdmin(admin.ModelAdmin):

    list_display = ('match', 'player', 'team')

admin.site.register(models.Bet, BetAdmin)
