from django.shortcuts import render, redirect
from manager.forms import LoginForm, CreatePoliceForm, CreateMissionForm, SendMessageForm
from . import db_funcs
from datetime import datetime

MANAGER_USERNAME = 'manager-username'


def index(request):
    return redirect('/manager/login/')


def home(request):
    # print(db_funcs.get_all_police())
    if is_manager_logged_in(request):
        return render(request, 'manager/home.html', {})
    else:
        return redirect('/manager/')


def sign_out(request):
    if is_manager_logged_in(request):
        del request.session[MANAGER_USERNAME]
    return redirect('/manager/')


def manager_authentication(username, password) -> bool:
    return username == 'admin' and password == 'admin'


def is_manager_logged_in(request):
    if request.session.get(MANAGER_USERNAME, None) is None:
        return False
    return True


def login_page(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if manager_authentication(username, form.cleaned_data['password']):
                request.session[MANAGER_USERNAME] = username
    else:
        form = LoginForm()

    if is_manager_logged_in(request):
        return redirect('/manager/home/')
    else:
        return render(request, 'manager/login.html', {'form': form})


def create_police(request):
    op_done = False
    fail_message = ''

    if not is_manager_logged_in(request):
        return redirect('/manager/')

    if request.method == 'POST':
        print(request.POST)
        form = CreatePoliceForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']

            try:
                db_funcs.create_police(username=username, password=password, name=name, gender=gender, birthday=birthday)
                op_done = True
            except Exception as err:
                op_done = False
                fail_message = str(err)

    else:
        form = CreatePoliceForm()

    if op_done:
        form = CreatePoliceForm()

    return render(request, 'manager/create_police.html', {'form': form, 'op_done': op_done, 'fail_message': fail_message})


def create_mission(request):
    op_done = False
    fail_message = ''

    if not is_manager_logged_in(request):
        return redirect('/manager/')

    if request.method == 'POST':
        print(request.POST)
        form = CreateMissionForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['location']
            description = form.cleaned_data['description']
            start_time = datetime.now()
            try:
                db_funcs.create_mission(loc=loc, st=start_time, desc=description)
                op_done = True
            except Exception as err:
                op_done = False
                fail_message = str(err)
    else:
        form = CreateMissionForm()

    return render(request, 'manager/create_mission.html', {'form': form, 'op_done': op_done, 'fail_message': fail_message})


def policemen_profile(request, username:str):
    op_done = False
    fail_message = ''

    if not is_manager_logged_in(request):
        return redirect('/manager/')

    police = db_funcs.get_police_username(username=username)

    if request.method == 'POST':
        print(request.POST)
        form = SendMessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            try:
                police.message_from_server = text
                police.save()
                op_done = True
            except Exception as err:
                op_done = False
                fail_message = str(err)
    else:
        form = SendMessageForm()

    return render(request, 'manager/policemen_profile.html',
                  {'op_done': op_done, 'fail_message': fail_message, 'form': form, 'police': police})