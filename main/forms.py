from django import forms

class UserCreateForm(forms.Form):
    user_num = forms.IntegerField(label='User_num')  # Field name made lowercase.
    user_id = forms.CharField(label='User_id', max_length=20)  # Field name made lowercase.
    user_password = forms.CharField(label='User_password', max_length=20)  # Field name made lowercase.
    user_nickname = forms.CharField(label='User_nickname', max_length=20)  # Field name made lowercase.
    user_email = forms.CharField(label='User_email', max_length=50)  # Field name made lowercase.
    user_profileurl = forms.CharField(label='User_profileurl', max_length=1000)  # Field name made lowercase.
    auth_id = forms.IntegerField(label='Auth_id')  # Field name made lowercase.
