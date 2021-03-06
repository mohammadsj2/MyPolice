from django.http import HttpResponse
from django.shortcuts import render, redirect
from manager.forms import LoginForm, CreatePoliceForm, CreateMissionForm, PoliceAssignForm, SendMessageForm
from . import db_funcs
from datetime import datetime

MANAGER_USERNAME = 'manager-username'


def index(request):
    """
    backend for rendering /manager url
    redirects to login page
    """
    return redirect('/manager/login/')


def home(request):
    """
    backend for rendering the manager home screen.
    redirects to login page if user isn't logged in
    """
    if is_manager_logged_in(request):
        return render(request, 'manager/home.html', {})
    else:
        return redirect('/manager/')


def sign_out(request):
    """
    backend for sign outing
    redirects to index page
    """
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
    """
    backend for login page
    if manager logged in: redirect home page
    """
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
    """
    backend for create police page
    """
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
                db_funcs.create_police(username=username, password=password, name=name, gender=gender,
                                       birthday=birthday)
                op_done = True
            except Exception as err:
                op_done = False
                fail_message = str(err)

    else:
        form = CreatePoliceForm()

    if op_done:
        form = CreatePoliceForm()

    return render(request, 'manager/create_police.html',
                  {'form': form, 'op_done': op_done, 'fail_message': fail_message})


def create_mission(request):
    """
    backend for create mission page
    """
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

    if op_done:
        form = CreateMissionForm()

    return render(request, 'manager/create_mission.html',
                  {'form': form, 'op_done': op_done, 'fail_message': fail_message})


def policemen_list(request):
    """
    backend for policemen list page
    """
    if not is_manager_logged_in(request):
        return redirect('/manager/')

    policemen = db_funcs.get_all_police()
    return render(request, 'manager/policemen_list.html',
                  {'policemen': policemen})


def policemen_profile(request, username: str):
    """
    backend for policemen profile page
    """
    op_done = False
    fail_message = ''

    if not is_manager_logged_in(request):
        return redirect('/manager/')

    police = db_funcs.get_police_by_username(username=username)

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


def mission_profile(request, mission_id):
    """
        backend for mission profile page
        """

    if not is_manager_logged_in(request):
        return redirect('/manager/')
    op_done = False
    fail_message = ""

    mission = db_funcs.get_mission(id=mission_id)
    if mission.end_time:
        assigned_police = db_funcs.get_mission_all_police(mission)
    else:
        assigned_police = db_funcs.get_mission_current_police(mission)
    if request.method == 'POST':
        print(request.POST)
        form = PoliceAssignForm(request.POST)
        if form.is_valid():
            policemen = form.cleaned_data['police']
            try:
                print(policemen)
                for police in policemen:
                    db_funcs.assign_police(mission, police)
                op_done = True
            except Exception as err:
                op_done = False
                fail_message = str(err)
    else:
        form = PoliceAssignForm()
    available_police = form.fields['police'].queryset
    return render(request, 'manager/mission_profile.html',
                  {'mission': mission, 'assigned_police': assigned_police, 'form': form, 'op_done': op_done,
                   'fail_message': fail_message, 'available_police': available_police})


def mission_list(request):
    """
    backend for mission list page
    """
    if not is_manager_logged_in(request):
        return redirect('/manager/')

    missions = db_funcs.get_all_missions()
    return render(request, 'manager/mission_list.html', {'missions': missions})


def end_mission(request, mission_id: int):
    """
    backend for ending mission
    redirects to index page
    """
    if not is_manager_logged_in(request):
        return redirect('/manager/')

    mission = db_funcs.get_mission(id=mission_id)
    db_funcs.end_mission(m=mission, end_time=datetime.now())
    return redirect('/manager/mission_profile/' + str(mission_id))
