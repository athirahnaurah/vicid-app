from django import forms
from .models import Users, History

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['profile_photo']

class ReportForm(forms.ModelForm):
    class Meta:
        model = History
        fields = []
       
    StartDate = forms.DateTimeField(
        label='Start Date',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
    )
    EndDate = forms.DateTimeField(
        label='End Date',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
    )