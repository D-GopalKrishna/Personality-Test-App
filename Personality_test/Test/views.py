
# from rest_framework import viewsets
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from django.http.response import HttpResponse, JsonResponse
# from .serializers import UserDataSerializer
# from .models import UserData, userSelection, MLmodelPasser



# def MLPass(request, user_id):
#     userdata = MLmodelPasser()

#     user_data = UserData.objects.get(url_key=user_id)
#     if request.method == 'GET':
#         userdata_serializer = UserDataSerializer(user_data) 
#         return JsonResponse(userdata_serializer.data)
#     elif request.method == 'PUT':
#         userdata = JSONParser().parse(request)
#         userdata_serializer = UserDataSerializer(user_data, data=userdata)
#         if userdata_serializer.is_valid():
#             userdata_serializer.save()
#             return JsonResponse(userdata_serializer.data)
#         return JsonResponse(userdata_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	