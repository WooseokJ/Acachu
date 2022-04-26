from django import forms
from main.models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_account', 'user_password']