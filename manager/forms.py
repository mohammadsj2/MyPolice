from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class CreatePoliceForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)
    name = forms.CharField(max_length=200, required=True)
    gender = forms.ChoiceField(choices=('Man', 'Female', 'Other'), required=True)
    birthday = forms.DateField()
