from dataclasses import fields
from django import forms
from main.models import Reply, AuthBoard


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_content']

class PostForm(forms.ModelForm):
    class Meta:
        model = AuthBoard
        fields = ['ab_title', 'ab_content']
