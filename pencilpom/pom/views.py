from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello! You're at the poms index.")
