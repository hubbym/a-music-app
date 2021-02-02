from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']