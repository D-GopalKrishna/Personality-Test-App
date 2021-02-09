from django.conf.urls import url
from django.core.files.base import endswith_cr
from rest_framework.serializers import Serializer
from Test.forms import UserNameForm
from typing import List
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from .models import UserChoice, UserName, Question
from .forms import UserChoiceForm, UserNameForm
from django.shortcuts import redirect
from django.db.models import Q

from django.forms import formset_factory, formsets
from rest_framework import viewsets
from .serializers import UserChoiceSerializer, UserNameSerializer, QuestionSerializer
# Create your views here.


# class HomeView(ListView):
# class TestView(ListView):
# class ResultView(ListView):



def HomeView(request):
	

	if request.method == 'POST':
		print(request.POST.get('username'))

		username = request.POST.get('username')

		obj = UserName.objects.filter(Q(username__iexact=username))
		# print(obj[0].url_key)
		# print(obj)

		# try:
		form = UserNameForm(data=request.POST)
		# 	print(form)
		# except:
		# 	print("form cannot be saved sorryyyy")
		# print(form)

		## If the user is already registered then don't submit the form but rather just taket her/his name and directly redirect to the test page with its uuid
		if obj:
			url_key = obj[0].url_key
			print(url_key)
			print("This is already there")
			return redirect('test', url_key= url_key)
		
		else:
			try:
				if form.is_valid():
					form.save()
					obj = UserName.objects.filter(Q(username__iexact=username))
					if obj:
						url_key = obj[0].url_key
						print(url_key)
						print("Created and now its there in the DB")
						return redirect('test', url_key= url_key)
			except:
				print("Not valid")
	else:
		form = UserNameForm()

	return render(request, "test/home.html", {'form':form})


    


def TestView(request, url_key):
	questions = Question.objects.all()
	username = UserName.objects.filter(Q(url_key__contains=url_key)).get()

	print(username.username)               ## Access in the templates as username.username

	if request.method=="POST":
		print(request.POST)
		print(request.POST.get('choices_for_q5'))
		form = UserChoiceForm(request.POST)
		UserChoiceFormSet = formset_factory(UserChoiceForm)
		formset = UserChoiceFormSet(request.POST)
		# print(formset)
		try:
			if formset.is_valid():
				for form in formset:
					print(form.cleaned_data)



				# choicy = form()
				# print(choicy)

				# for i in range(50):
				# 	print(questions[i])
				# 	print(request.POST.get('choices_for_q{}'.format(i)))
				# 	# choicy = form.save(commit=False)
				# 	choicy.user = username.username
				# 	choicy.question_number = questions[i]
				# 	choicy.choices = request.POST.get('choices_for_q{}'.format(i))
				# 	choicy.save()
		except:
			print("Form is not valid")
	else:
		form = UserChoiceForm()

	return render(request, "test/taketest.html", {"questions":questions, "username":username, "form":form})


def ResultView(request, url_key):
	obj = get_object_or_404(UserName, url_key=url_key)
	print(obj)
	return render(request, "test/results.html", {'urk_':obj.url_key})




## ____________________________________________________
# Serializers



# class QuestionViewSet(viewsets.ModelViewSet):
# 	queryset = Question.objects.all()
# 	serializer_class = QuestionSerializer

