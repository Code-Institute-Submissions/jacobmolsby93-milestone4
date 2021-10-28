from .models import Member
from django import forms


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
