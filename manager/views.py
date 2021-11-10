from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, <b>manager</b>. You're at the manager index.")
