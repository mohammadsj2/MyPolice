from django.shortcuts import render, redirect
from manager.forms import LoginForm

MANAGER_USERNAME = 'manager-username'


def index(request):
    return redirect('/manager/login/')


def home(request):
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
    else:
        form = LoginForm()

    if is_manager_logged_in(request):
        return redirect('/manager/home/')
    else:
        return render(request, 'manager/login.html', {'form': form})
