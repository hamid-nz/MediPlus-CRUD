from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def all_users(request):
    return HttpResponse("Returning Http Response")

