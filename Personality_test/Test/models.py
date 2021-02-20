from typing import Match
from django.db import models
from django.db.models.base import Model
from django.db import models
import uuid
from django.db.models.query_utils import Q
from django.dispatch import receiver
from django.db.models.signals import post_save

import os
import numpy as np
from pickle import load
# from .views import MLPass

# _____________________________________________

class UserData(models.Model):
    username = models.CharField(max_length=50) 
    url_key = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, blank=True, editable=False)     ## creating a uuid for every user
    # url_key = models.SlugField(primary_key=True)
    personality_type = models.IntegerField(null=True, blank=True,)     ## blank related to validation (that blank values are allowed to be submitted), on the other hand null=True is database related (that if any blank value is there then DB will set it to null)
    extroversion_score = models.IntegerField(null=True, blank=True)
    neurotic_score = models.IntegerField(null=True, blank=True)
    agreeable_score = models.IntegerField(null=True, blank=True)
    conscientious_score = models.IntegerField(null=True, blank=True)
    open_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.url_key)
    

class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question




class userSelection(models.Model):
    CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    user = models.OneToOneField(UserData, null=True, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q2 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q3 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q4 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q5 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q6 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q7 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q8 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q9 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q10 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q11 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q12 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q13 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q14 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q15 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q16 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q17 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q18 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q19 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q20 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q21 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q22 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q23 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q24 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q25 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q26 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q27 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q28 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q29 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q30 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q31 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q32 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q33 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q34 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q35 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q36 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q37 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q38 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q39 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q40 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q41 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q42 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q43 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q44 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q45 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q46 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q47 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q48 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q49 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)
    q50 = models.CharField(max_length=2, choices=CHOICES, blank=False, null=False)

    # def __repr__(self):
    #     return self.user






@receiver(post_save,sender=userSelection)
def MLmodelPasser(created,instance,*args,**kwargs):
    if created:
        module_dir = os.path.dirname(__file__) 
        print(module_dir)
        model_k_fit = load(open(os.path.join(module_dir, "ml_models/ml_unsupervised_model_personality_test.pkl"), 'rb'))
        min_max_scaler = load(open(os.path.join(module_dir,"ml_models/scaler.pkl"), 'rb'))

        user_input = userSelection.objects.get(user=instance.user)
        print('hi')

        print(type(user_input))
        print(type(user_input.q1))
        listy = []
        listy.append(user_input.q1)
        listy.append(user_input.q2)
        listy.append(user_input.q3)
        listy.append(user_input.q4)
        listy.append(user_input.q5)
        listy.append(user_input.q6)
        listy.append(user_input.q7)
        listy.append(user_input.q8)
        listy.append(user_input.q9)
        listy.append(user_input.q10)
        listy.append(user_input.q11)
        listy.append(user_input.q12)
        listy.append(user_input.q13)
        listy.append(user_input.q14)
        listy.append(user_input.q15)
        listy.append(user_input.q16)
        listy.append(user_input.q17)
        listy.append(user_input.q18)
        listy.append(user_input.q19)
        listy.append(user_input.q20)
        listy.append(user_input.q21)
        listy.append(user_input.q22)
        listy.append(user_input.q23)
        listy.append(user_input.q24)
        listy.append(user_input.q25)
        listy.append(user_input.q26)
        listy.append(user_input.q27)
        listy.append(user_input.q28)
        listy.append(user_input.q29)
        listy.append(user_input.q30)
        listy.append(user_input.q31)
        listy.append(user_input.q32)
        listy.append(user_input.q33)
        listy.append(user_input.q34)
        listy.append(user_input.q35)
        listy.append(user_input.q36)
        listy.append(user_input.q37)
        listy.append(user_input.q38)
        listy.append(user_input.q39)
        listy.append(user_input.q40)
        listy.append(user_input.q41)
        listy.append(user_input.q42)
        listy.append(user_input.q43)
        listy.append(user_input.q44)
        listy.append(user_input.q45)
        listy.append(user_input.q46)
        listy.append(user_input.q47)
        listy.append(user_input.q48)
        listy.append(user_input.q49)
        listy.append(user_input.q50)
        

        

        # for i in range(1, 51):
        #     # listy.append(user_input.q'{0}')
        #     listy.append(user_input.('q{0}'.format(i)))

        print(listy)
        print('hi')

        user_input = np.array(listy).reshape(1,-1)
        user_input = min_max_scaler.transform(user_input)
        user_personality = model_k_fit.predict(user_input)   

        col_list = user_input[0]
        ext = col_list[0:10]
        est = col_list[10:20]
        agr = col_list[20:30]
        csn = col_list[30:40]
        opn = col_list[40:50]

        ext = np.array([sum(ext)], dtype='int32')
        est = np.array([sum(est)], dtype='int32')
        agr = np.array([sum(agr)], dtype='int32')
        csn = np.array([sum(csn)], dtype='int32')
        opn = np.array([sum(opn)], dtype='int32')

        userdata = {
            "extroversion_score":ext[0],
            "neurotic_score":est[0],
            "agreeable_score":agr[0],
            "conscientious_score":csn[0],
            "open_score":opn[0],
            "personality_type":user_personality[0]
        }
        print(userdata)
        print(instance.user)
        ## Put section
        user_data = UserData.objects.get(url_key=uuid.UUID(str(instance.user))) 
        user_data.personality_type = userdata['personality_type']
        user_data.extroversion_score = userdata['extroversion_score']
        user_data.neurotic_score = userdata['neurotic_score']
        user_data.agreeable_score = userdata['agreeable_score']
        user_data.conscientious_score = userdata['conscientious_score']
        user_data.open_score = userdata['open_score']
        user_data.save()

        print(user_data)
        # return userdata










# @receiver(post_save, sender=userSelection)
# def ensure_profile_exists(sender, **kwargs):
#     if kwargs.get('created', False):
#         UserData.objects.get_or_create(user=kwargs.get('instance'))









# class UserChoice(models.Model):
#     QUESTION_CHOICES = (
#         ("1", "1"),
#         ("2", "2"),
#         ("3", "3"),
#         ("4", "4"),
#     )
#     user = models.ForeignKey(UserData, on_delete=models.CASCADE)
#     question_number = models.ManyToManyField(Question, verbose_name="questions_number")
#     choices = models.CharField(max_length=20, choices=QUESTION_CHOICES, blank=True)













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


