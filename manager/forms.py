from django import forms
from location_field.forms.plain import PlainLocationField

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class CreatePoliceForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=200, required=True)
    name = forms.CharField(max_length=200, required=True)
    gender = forms.ChoiceField(choices=(('1', 'Male'), ('2', 'Female')))
    birthday = forms.DateField()


class CreateMissionForm(forms.Form):
    description = forms.CharField(max_length=2000)
    location = PlainLocationField(based_fields=['city'],
                                  initial='-22.2876834,-49.1607606')