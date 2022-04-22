from django import forms
from main.models import *

class ReplyForm(forms.ModelForm):
    store_id = forms.IntegerField(max_value=None)
    reply_content = forms.CharField(max_length=300, required=True)