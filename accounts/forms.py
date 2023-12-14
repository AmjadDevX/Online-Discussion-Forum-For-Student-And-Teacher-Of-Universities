from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    # mid_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('first_name','last_name' , 'username', 'email', 'password1', 'password2')