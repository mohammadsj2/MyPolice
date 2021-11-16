from .models import *
from django.utils.timezone import now


def get_all_police():
    return Police.objects.all()

def get_available_police():
    return Police.objects.filter(status='available')

def get_police(id):
    return Police.objects.get(pk=id)


def get_police_by_username(username):
    try:
        return Police.objects.get(username=username)
    except Exception:
        return None

def get_all_missions():
    return Mission.objects.all()


def get_mission(id):
    return Mission.objects.get(id=id)


def get_missions_by_loc(loc):
    return Mission.objects.filter(location=loc)


def get_mission_current_police(m: Mission):
    return m.current_police.all()


def get_mission_all_police(m: Mission):
    return m.all_police.all()


def create_mission(loc, st=now(), desc=''):
    m = Mission(location=loc, start_time=st, description=desc)
    m.save()
    return m


def set_mission_loc(m: Mission, loc):
    m.location = loc
    m.save()


def set_mission_desc(m: Mission, desc):
    m.description = desc
    m.save()


def assign_police(m: Mission, p: Police, join_time=now()):
    m.current_police.add(p)
    p.status = 'unavailable'
    p.save()
    m.all_police.add(p, through_defaults={"join_time": join_time})


def create_mission_assign_police(police_list: list, loc, st=now(), desc=''):
    m = create_mission(loc, st, desc)
    for p in police_list:
        assign_police(m, p, st)
    return m


def unassign_police(m: Mission, p: Police, leave_time=now()):
    p.status = 'available'
    p.save()
    mp = MissionPolice.objects.get(mission=m, police=p)
    mp.leave_time = leave_time
    mp.save()
    return mp


def end_mission(m: Mission, end_time=now()):
    for p in get_mission_current_police(m):
        unassign_police(m, p, end_time)
    m.end_time = end_time
    m.save()


def create_police(username, password, name, gender, birthday):
    p = Police(username=username, password=password, name=name, gender=gender, birthday=birthday, status='available')
    p.save()
    return p


def set_police_username(p: Police, username):
    p.username = username
    p.save()


def set_police_password(p: Police, password):
    p.password = password
    p.save()


def set_police_name(p: Police, name):
    p.name = name
    p.save()


def set_police_gender(p: Police, gender):
    p.gender = gender
    p.save()


def set_police_birthday(p: Police, birthday):
    p.birthday = birthday
    p.save()


def set_police_location(p: Police, location):
    p.location = location
    p.save()


def set_police_status(p: Police, status):
    p.status = status
    p.save()
