from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, <b>police officer</b>. You're at the police index.")
