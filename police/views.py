from django.shortcuts import render, redirect
import manager.db_funcs as db_funcs
from manager.forms import LoginForm
from django.http import HttpResponse

from manager.models import Police

USERNAME_FIELD = "username"


def index(request):
    return redirect('/police/login')


def home(request):
    if is_user_logged_in(request):
        return render(request, 'police/home.html',
                      {'name': db_funcs.get_police_by_username(request.session[USERNAME_FIELD]).name})
    else:
        return redirect('/police/')

def mission(request):
    if not is_user_logged_in(request):
        return redirect('/police/')
    
    police: Police = db_funcs.get_police_by_username(request.session[USERNAME_FIELD])
    mission = police.current_mission
    return render(request, 'police/mission.html', {'mission': mission})

def sign_out(request):
    if is_user_logged_in(request):
        del request.session[USERNAME_FIELD]
    return redirect('/police/')


def login_authentication(username, password) -> bool:
    police = db_funcs.get_police_by_username(username)
    if police is None:
        return False
    if police.password != password:
        return False
    return True


def is_user_logged_in(request):
    if request.session.get(USERNAME_FIELD, None) is None:
        return False
    return True


def login_page(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if login_authentication(username, form.cleaned_data['password']):
                request.session[USERNAME_FIELD] = username
    else:
        form = LoginForm()

    if is_user_logged_in(request):
        return redirect('/police/home/')
    else:
        return render(request, 'police/login.html', {'form': form})
