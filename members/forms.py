from .models import Member
from django import forms
from django.contrib.auth.forms import UserChangeForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'first_name', 
            'last_name',
            'email',
            'profile_image',
            'description'
        ]


class EditProfileForm(UserChangeForm):
    class Meta:
        model = Member
        fields = [
            'first_name', 
            'last_name',
            'email',
            'profile_image',
            'description'
        ]