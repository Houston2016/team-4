from __future__ import unicode_literals

from django.db import models

class CardModel(models.Model):
    """
    a card of card submission
    """
    title = models.CharField(blank=False, max_length=52)
    weight = models.IntegerField()

class CardSubmissionModel(models.Model):
    """
    An obbject representing the prefrences of a given user.
    """

    submission = models.ManyToManyField(CardModel)

class Themes(models.Model):
    """
    An object represent one of the many themes given by admins
    """

    name = models.CharField(blank=False, max_length=52)
    description = models.CharField(max_length=240)

class MatteModel(models.Model):
    """
    This is a model representing the mat that is done at a community event.
    """

    title = models.CharField(blank=False, max_length=52)
    description = models.CharField(max_length=240)
    themes = models.ManyToManyField(Themes)
    submissions = models.ManyToManyField(CardSubmissionModel)

