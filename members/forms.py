from .models import Member
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ProfileForm(UserChangeForm):
    class Meta:
        model = Member
        fields = [
            'first_name', 
            'last_name',
            'email',
            'profile_image',
            'description'
        ]