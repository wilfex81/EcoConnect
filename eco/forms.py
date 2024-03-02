from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'interests', 'skills', 'contributions']
