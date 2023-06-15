from django import forms
from django.contrib.auth.models import User
from .models import Chatroom,UserProfile

class ChatroomForm(forms.ModelForm):
    class Meta:
        model = Chatroom
        fields = ['name', 'slug']

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Chatroom.objects.filter(slug=slug).exists():
            raise forms.ValidationError('This slug is already in use.')
        return slug


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name' ,'last_name','username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('avatar','bio')
