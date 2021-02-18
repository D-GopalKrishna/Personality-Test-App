from django.http.response import JsonResponse
from .models import Question, UserData, userSelection, MLmodelPasser
from rest_framework import viewsets, permissions, mixins, generics
from .serializers import QuestionSerializer, UserDataSerializer, userSelectionSerializer
# from rest_framework.views import APIView

import numpy as np
from pickle import load
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import HttpResponse, JsonResponse, Http404

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer


# class UserChoiceViewset(viewsets.ModelViewSet):
#     queryset = UserChoice.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = UserChoiceSerializer


class UserDataViewset(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserDataSerializer


# class UserDataDetailViewset(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    # queryset = UserData.objects.all()
    # serializer_class = UserDataSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)


    # def get(self, request, user_id, *args, **kwargs):
    #     user_data = UserData.objects.get(url_key=user_id)
    #     serializer = UserDataSerializer(user_data, many=True)
    #     return JsonResponse(serializer.data)

    # def post(self, request, format=None):
    #     userdata = MLmodelPasser()
    #     serializer = UserDataSerializer(data=userdata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class userSelectionViewset(viewsets.ModelViewSet):
    queryset = userSelection.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = userSelectionSerializer

