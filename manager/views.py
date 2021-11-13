from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return redirect('login')


def login_page(request):
    context = {}
    return render(request, 'manager/login.html', context)
