from django.db.models import fields
from rest_framework import serializers
from .models import UserData, Question, userSelection


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

# class UserChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserChoice
#         fields = "__all__"


class userSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSelection
        fields = "__all__"
