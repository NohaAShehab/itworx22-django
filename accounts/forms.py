from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpCustomizedForm(UserCreationForm):
    first_name= forms.CharField(max_length=30, required=False, help_text="Optional ... ")
    last_name= forms.CharField(max_length=30, required=False, help_text="Optional ... ")
    email= forms.EmailField(max_length=30, required=True, help_text="Required ... ")
    is_staff = forms.BooleanField(
        help_text="Designates whether the user can log into this admin site.",
    )

    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff')
