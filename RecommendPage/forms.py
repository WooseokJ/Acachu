from dataclasses import fields
from django import forms
from main.models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'store', 'review_content']
