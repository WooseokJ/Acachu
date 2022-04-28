from dataclasses import fields
from django import forms
from main.models import *

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_content']