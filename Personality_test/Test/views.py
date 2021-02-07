from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.


# class HomeView(ListView):
# class TestView(ListView):
# class ResultView(ListView):



def HomeView(request):
    return HttpResponse("Hi This is HomeView")


def TestView(request):
    return HttpResponse("Hi This is TestView")


def ResultView(request):
    return HttpResponse("Hi This is ResultView")
