from django.db.models import fields
from rest_framework import serializers
from .models import UserChoice, UserName, Question


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoice
        fields = "__all__"
