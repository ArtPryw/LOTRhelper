from django.shortcuts import render
from django.http import HttpResponse


def game(request):
    return HttpResponse("This is a main site of LOTR RPG Game!")
# Create your views here.
