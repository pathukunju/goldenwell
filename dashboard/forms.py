from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'email@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

    class Meta:
        model= User
        field = ['email','password']


    def clean(self):
        cleaned_data = super().clean()
        password=cleaned_data.get("password")