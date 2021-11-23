from django.shortcuts import render, redirect
import manager.db_funcs as db_funcs
from manager.forms import LoginForm
from django.http import HttpResponse

from manager.models import Police

USERNAME_FIELD = "username"


def index(request):
    """

    backend for rendering index page
    redirects to login
    """

    return redirect('/police/login')


def home(request):
    """

    backend for rendering the police home screen.
    redirects to login page if user isn't logged in
    updates officer location in database
    """
    if is_user_logged_in(request):
        if update_user_location(request):
            return redirect("/police/home")
        return render(request, 'police/home.html',
                      {'name': db_funcs.get_police_by_username(request.session[USERNAME_FIELD]).name})
    else:
        return redirect('/police/')


def mission(request):
    """

    backend for rendering the police mission screen.
    redirects to login page if user isn't logged in
    updates officer location in database
    sends mission information to front-end
    """

    if not is_user_logged_in(request):
        return redirect('/police/')
    if update_user_location(request):
        return redirect('/police/mission')
    police: Police = db_funcs.get_police_by_username(request.session[USERNAME_FIELD])
    mission = police.current_mission
    return render(request, 'police/mission.html',
                  {'mission': mission, 'name': db_funcs.get_police_by_username(request.session[USERNAME_FIELD]).name})


def update_user_location(request):
    """

    updates user location based on request POST content
    """
    if request.method == 'POST':
        print(request.POST)
        latitude = request.POST["lat"]
        longitude = request.POST["long"]
        try:
            police = db_funcs.get_police_by_username(request.session[USERNAME_FIELD])
            db_funcs.set_police_location(police, latitude + ', ' + longitude)
        except Exception as err:
            print(err)
        return True
    else:
        return False


def sign_out(request):
    """

    signs user out of current session
    """

    if is_user_logged_in(request):
        del request.session[USERNAME_FIELD]
    return redirect('/police/')


def login_authentication(username, password) -> bool:
    """

    authenticates the username and password using the database
    """

    police = db_funcs.get_police_by_username(username)
    if police is None:
        return False
    if police.password != password:
        return False
    return True


def is_user_logged_in(request):
    """

    checks if the user is logged in
    """

    if request.session.get(USERNAME_FIELD, None) is None:
        return False
    return True


def login_page(request):
    """
        backend for rendering the login page
    """
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
        return render(request, 'police/login.html',
                      {'form': form})


def notifications(request):
    """

    backend for rendering the police notifications screen.
    redirects to login page if user isn't logged in
    updates officer location in database
    sends notification to front-end
    """
    if not is_user_logged_in(request):
        return redirect('/police/')
    if update_user_location(request):
        return redirect('/police/notifications')
    police: Police = db_funcs.get_police_by_username(request.session[USERNAME_FIELD])
    message = police.message_from_server
    return render(request, 'police/notifications.html',
                  {'message': message, 'name': db_funcs.get_police_by_username(request.session[USERNAME_FIELD]).name})
