from django.shortcuts import render
from django.http import HttpResponse
def say(request):
    return HttpResponse('hello neelima')
# Create your views here.
