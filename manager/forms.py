from django import db, forms
from django.forms.forms import Form
from manager import db_funcs

from manager.models import Police


# from location_field.forms.plain import PlainLocationField

# In this file we create necessary forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CreatePoliceForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               max_length=200, required=True)
    name = forms.CharField(max_length=200, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    gender = forms.ChoiceField(choices=(('1', 'Male'), ('2', 'Female')),
                               widget=forms.Select(attrs={'class': 'form-select'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birthday'}),
                               label='Birthday (YYYY-MM-DD)')


class CreateMissionForm(forms.Form):
    location = forms.CharField(label='Location (x, y)', max_length=40, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
    description = forms.CharField(label='Description', max_length=200,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))


class SendMessageForm(forms.Form):
    text = forms.CharField(label='Message', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Message',
               'style': 'height: 150px;'}), max_length=2000, required=True)


class PoliceAssignForm(forms.Form):
    police = forms.ModelMultipleChoiceField(queryset=db_funcs.get_available_police(), widget=forms.SelectMultiple)
