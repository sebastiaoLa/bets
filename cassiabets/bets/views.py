# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy

from bets import models, forms


# ====================================
# Matches
# ====================================
class MatchesView(generic.ListView):

    template_name = 'matches/list.html'

    def get_queryset(self):
        return models.Match.objects.all()

# ====================================
class MatchesDetailsView(generic.DetailView):

    model = models.Match
    template_name = 'matches/detail.html'

# ====================================
class MatchesCreateView(generic.CreateView):

    model = models.Match
    template_name = 'matches/form.html'
    success_url = reverse_lazy('bets:match-list')
    form_class = forms.MatchForm

# ====================================
# Teams
# ====================================
class TeamsView(generic.ListView):

    template_name = 'teams/list.html'

    def get_queryset(self):
        return models.Team.objects.all()

# ====================================
class TeamDetailsView(generic.DetailView):

    model = models.Team
    template_name = 'teams/detail.html'

# ====================================
class TeamDetails2View(generic.DetailView):

    model = models.Team
    template_name = 'teams/detail.html'

    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(models.Team, name=name)

# ====================================
class TeamCreateView(generic.CreateView):

    model = models.Team
    template_name = 'teams/form.html'
    success_url = reverse_lazy('bets:team-list')
    form_class = forms.TeamForm

# ====================================
# Player
# ====================================
class PlayerView(generic.ListView):

    template_name = 'player/list.html'

    def get_queryset(self):
        return models.Player.objects.all()

# ====================================
class PlayerDetailsView(generic.DetailView):

    model = models.Player
    template_name = 'player/detail.html'

# ====================================
class PlayerCreateView(generic.CreateView):

    model = models.Player
    template_name = 'player/form.html'
    success_url = reverse_lazy('bets:player-list')
    form_class = forms.PlayerForm

# ====================================
# Bet
# ====================================
class BetView(generic.ListView):

    template_name = 'bet/list.html'

    def get_queryset(self):
        return models.Bet.objects.all()

# ====================================
class BetDetailsView(generic.DetailView):

    model = models.Bet
    template_name = 'bet/detail.html'

# ====================================
class BetCreateView(generic.CreateView):

    model = models.Bet
    template_name = 'bet/form.html'
    success_url = reverse_lazy('bets:bet-list')
    form_class = forms.BetForm
