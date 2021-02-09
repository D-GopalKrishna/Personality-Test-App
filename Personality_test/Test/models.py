from typing import Match
from django.db import models
from django.db.models.base import Model
from django.db import models
import uuid
from django.db.models.query_utils import Q

# _____________________________________________

class UserName(models.Model):
    username = models.CharField(max_length=50) 
    url_key = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, auto_created=True, editable=False)     ## creating a uuid for every user
    personality_type = models.IntegerField(null=True, blank=True,)     ## blank related to validation (that blank values are allowed to be submitted), on the other hand null=True is database related (that if any blank value is there then DB will set it to null)


class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question



class UserChoice(models.Model):
    QUESTION_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    user = models.ForeignKey(UserName, on_delete=models.CASCADE)
    question_number = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.CharField(max_length=20, choices=QUESTION_CHOICES, blank=True)

    # choice = models.IntegerField()




# class Choices(models.Model):
#     QUESTION_CHOICES = (
#         ("1", "1"),
#         ("2", "2"),
#         ("3", "3"),
#         ("4", "4"),
#     )
#     choices = models.CharField(max_length=20, choices=QUESTION_CHOICES, blank=True)




# class TestRecord(models.Model):             ## This will be available for every unique user which can be accessed in results.
#     username = models.CharField(primary_key=True, max_length=100, unique=True)          ## User's accessing their results via their unique username
#     personality_type = models.IntegerField(null=True, blank=True,)              ## From the personality types that we created via ml model

    

    ## Once the user takes the test personality_type should get updated
    ## (Later we can create the whole graph and show the different levels of personaloity via just the personality type.) 
    # (Personality type between [0,1,2,3,4])\

    ## .........

    # def __str__(self):
    #     return self.username



# class UserChoices(models.Model):
#     user = models.ForeignKey('TestRecord', on_delete=models.CASCADE)
#     choices = models.('Questions')               ## The choices are actually integers, but I am taking charfield because I took so in Question model. This can later be converted to integer by int() function.


