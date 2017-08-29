# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from bets import views

urlpatterns = [
    # Views
    url(r'^matches/$', views.MatchesView.as_view(), name='match-list'),
    url(r'^matches/(?P<pk>[0-9]+)/$', views.MatchesDetailsView.as_view(), name='match-details'),
    url(r'^matches/create/$', views.MatchesCreateView.as_view(), name='match-create'),


    url(r'^players/$', views.PlayerView.as_view(), name='player-list'),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetailsView.as_view(), name='player-details'),
    url(r'^players/create/$', views.PlayerCreateView.as_view(), name='player-create'),


    url(r'^bets/$', views.BetView.as_view(), name='bet-list'),
    url(r'^bets/(?P<pk>[0-9]+)/$', views.BetDetailsView.as_view(), name='bet-details'),
    url(r'^bets/create/$', views.BetCreateView.as_view(), name='bet-create'),

    url(r'^teams/$', views.TeamsView.as_view(), name='team-list'),
    url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetailsView.as_view(), name='team-details'),
    # url(r'^teams/(?P<name>[\w]+)/$', views.TeamDetails2View.as_view(), name='team-details-2'),
    url(r'^teams/create/$', views.TeamCreateView.as_view(), name='team-create'),
]
