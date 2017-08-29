# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models

# ====================================
# Apostador
# ====================================
class Player(models.Model):

    name = models.CharField(
        'nome',
        max_length=255
    )

    points = models.PositiveIntegerField(
        'pontos',
        default=0
    )

    cash = models.FloatField(
        'dinheiro',
        default=0
    )

    status = models.BooleanField(
        'ativo',
        default=True
    )

    def __str__(self):
        return "%s (%d)" % (self.name, self.cash)

    def __unicode__(self):
        return unicode("%s (%d)" % (self.name, self.cash))

    class Meta:
        verbose_name = 'apostador'
        verbose_name_plural = 'apostadores'
        ordering = ['name']

# ====================================
# Time
# ====================================
class Team(models.Model):

    name = models.CharField(
        'nome',
        max_length=255
    )

    points = models.PositiveIntegerField(
        'pontos',
        default=0
    )

    def __str__(self):
        return "%s (%d)" % (self.name, self.points)

    def __unicode__(self):
        return unicode("%s (%d)" % (self.name, self.points))

    class Meta:
        verbose_name = 'time'
        verbose_name_plural = 'times'
        ordering = ['name']

# ====================================
# Partida
# ====================================
class Match(models.Model):

    team_1 = models.ForeignKey(
        Team,
        related_name='team_1'
    )

    team_2 = models.ForeignKey(
        Team,
        related_name='team_2'
    )

    winner = models.ForeignKey(
        Team,
        related_name='winner',
        blank=True,
        null=True
    )

    tie = models.BooleanField(
        'empate',
        default=False
    )

    date = models.DateField(
        'data',
        default=datetime.date.today
    )

    def __str__(self):
        return "%s x %s" % (self.team_1, self.team_2)

    def __unicode__(self):
        return unicode("%s x %s" % (self.team_1, self.team_2))

    class Meta:
        verbose_name = 'partida'
        verbose_name_plural = 'partidas'
        ordering = ['team_1']

# ====================================
# Aposta
# ====================================
class Bet(models.Model):

    match = models.ForeignKey(
        Match,
        related_name='bet'
    )

    team = models.ForeignKey(
        Team,
        related_name='bet'
    )

    player = models.ForeignKey(
        Player,
        related_name='bet'
    )

    def __str__(self):
        return "%s %s %s" % (self.match, self.player, self.team)

    def __unicode__(self):
        return unicode("%s %s %s" % (self.match, self.player, self.team))

    class Meta:
        verbose_name = 'aposta'
        verbose_name_plural = 'apostas'
        ordering = ['match']
