from os import stat
from django.conf.urls import url
from django.core.files.base import endswith_cr
from rest_framework.serializers import Serializer
from typing import List
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic.list import ListView
from django.db.models import Q

from django.forms import formset_factory, formsets
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import UserChoice, UserData, Question, userSelection
from .forms import UserChoiceForm, UserDataForm, userSelectionForm
from .serializers import UserDataSerializer

import numpy as np
from pickle import load
#____________________________________________________________________

# class HomeView(ListView):
# class TestView(ListView):
# class ResultView(ListView):



def HomeView(request):
	

	if request.method == 'POST':
		print(request.POST.get('username'))

		username = request.POST.get('username')

		obj = UserData.objects.filter(Q(username__iexact=username))
		# print(obj[0].url_key)
		# print(obj)

		# try:
		form = UserDataForm(data=request.POST)
		# 	print(form)
		# except:
		# 	print("form cannot be saved sorryyyy")
		# print(form)

		## If the user is already registered then don't submit the form but rather just taket her/his name and directly redirect to the test page with its uuid
		if obj:
			url_key = obj[0].url_key
			print(url_key)
			print("This is already there")
			return redirect('Test:test', url_key= url_key)
		
		else:
			try:
				if form.is_valid():
					form.save()
					obj = UserData.objects.filter(Q(username__iexact=username))
					if obj:
						url_key = obj[0].url_key
						print(url_key)
						print("Created and now its there in the DB")
						return redirect('Test:test', url_key=url_key)
			except:
				print("Not valid")
	else:
		form = UserDataForm()

	return render(request, "test/home.html", {'form':form})




	# user_data = UserName.objects.get(url_key=user_id)
	# if request.method == 'GET':
	# 	userdata_serializer = UserNameSerializer(user_data) 
    #     return JsonResponse(userdata_serializer.data) 
	





def TestView1(request, url_key):
	print("hi", request.POST)

	if request.method=="POST":
		user_selection_form = userSelectionForm(request.POST)
		print("hi", request.POST.get())
		if user_selection_form:
			user_selection_form.save()
			# print(user_selection_form)
			return redirect('Test:test', url_key=url_key)

		
	else:
		user_selection_form = userSelectionForm()

	return render(request, "test/taketest1.html", {"user_selection_form": user_selection_form})



    


def TestView2(request, url_key):
	questions = Question.objects.all()
	username = UserData.objects.filter(Q(url_key__contains=url_key)).get()

	print("hi",username.username)               ## Access in the templates as username.username

	if request.method=="POST":
		print(request.POST)
		print(request.POST.get('choices_for_q5'))
		form = UserChoiceForm(request.POST)
		# print("Form : ", form)
		# UserChoiceFormSet = formset_factory(UserChoiceForm)
		# formset = UserChoiceFormSet(request.POST)
		# print(formset)
		try:
			print("hi")

			if form:
				print("hihi")
				# print(form)
				form.save()

			# if form.is_valid():
				# for form in form:
				# 	print(form.cleaned_data)

			# if form:
			# 	print("Hi ")
			# 	choicy = form()
			# 	print(choicy)

			# 	for i in range(50):
			# 		print(questions[i])
			# 		print(request.POST.get('choices_for_q{}'.format(i)))
			# 		# choicy = form.save(commit=False)
			# 		choicy.user = username.username
			# 		choicy.question_number = questions[i]
			# 		choicy.choices = request.POST.get('choices_for_q{}'.format(i))
			# 		choicy.save()
			# # 		print(choicy)
			# else:
			# 	print("Hi second")
		except:
			print("Form is not valid")
	else:
		form = UserChoiceForm()
		return render(request, "test/taketest2.html", {"questions":questions, "username":username, "form":form})

	# return render(request, "test/taketest.html")



def ResultView(request, url_key):
	obj = get_object_or_404(UserData, url_key=url_key)
	print(obj)
	return render(request, "test/results.html", {'urk_':obj.url_key})


