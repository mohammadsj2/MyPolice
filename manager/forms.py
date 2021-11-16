from django import db, forms
from django.forms.forms import Form
from manager import db_funcs

from manager.models import Police


# from location_field.forms.plain import PlainLocationField

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class CreatePoliceForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200, required=True)
    name = forms.CharField(max_length=200, required=True)
    gender = forms.ChoiceField(choices=(('1', 'Male'), ('2', 'Female')))
    birthday = forms.DateField()


class CreateMissionForm(forms.Form):
    location = forms.CharField(label='Location (x, y)', max_length=40, required=True)
    description = forms.CharField(max_length=200)


class SendMessageForm(forms.Form):
    text = forms.CharField(label='Text', widget=forms.Textarea, max_length=2000, required=True)


class PoliceAssignForm(forms.Form):
    police = forms.ModelMultipleChoiceField(queryset=db_funcs.get_available_police(), widget=forms.SelectMultiple)
