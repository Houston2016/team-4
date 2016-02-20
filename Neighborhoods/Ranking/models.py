from __future__ import unicode_literals

from django.db import models
import random
import json

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

    def to_json(self):
        json_resp = {'title': self.title,
                'description': self.description,
                'themes': self.get_themes(),
                'submissions': self.get_submissions()}
        return dict(json_resp)

    def get_themes(self):
        return list(self.themes.all())

    def get_submissions(self):
        everything = []
        for total_submission in self.submissions.all():
            temp_sub = []
            for card in total_submission.submission.all():
                temp_sub.append({card.title: card.weight})
            everything.append(temp_sub)

        return everything

def populate_db():
    submittedthemes = ['Robotics', 'Sewing', 'Commercial Kitchen', 'Place to make new products', 'Woodworking', 'Focus on future tools',
                       'Inter-age activities', 'tools', 'Quite Classroom', 'Machinery', 'Metalworking', 'Different short classes',
                       'Art Space', 'Focus on youth', 'Shared knowledge', 'Electronics', 'Skilled tutors', 'Computer Skills',
                       'Jewelery making']

    my_matt = MatteModel(title='Maker Space', description='Let us make things together')
    my_matt.save()
    for theme in submittedthemes:
        temp_theme = Themes(name=theme)
        temp_theme.save()
        my_matt.themes.add(temp_theme)

    themes_to_choose = [theme.name for theme in my_matt.themes.all()]

    for i in range(10):
        new_submission = CardSubmissionModel()
        new_submission.save()
        points_to_give = [1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,5,5]
        random.shuffle(points_to_give)

        for th in themes_to_choose:
            choice = random.choice(points_to_give)
            new_card = CardModel(title=th, weight=choice)
            new_card.save()
            new_submission.submission.add(new_card)
            points_to_give.remove(choice)

        my_matt.submissions.add(new_submission)