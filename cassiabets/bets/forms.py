# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from bets import models


# ================================
# Team
# ================================
class TeamForm(forms.ModelForm):

    class Meta:
        model = models.Team
        fields = ('__all__')

# ================================
# Match
# ================================
class MatchForm(forms.ModelForm):

    class Meta:
        model = models.Match
        fields = ('__all__')

# ================================
# Player
# ================================
class PlayerForm(forms.ModelForm):

    class Meta:
        model = models.Player
        fields = ('__all__')

# ================================
# Bet
# ================================
class BetForm(forms.ModelForm):

    class Meta:
        model = models.Bet
        fields = ('__all__')
