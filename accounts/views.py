from django.shortcuts import render
from  django.views.generic.edit import CreateView
# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
# def signup():
#     pass
from accounts.forms import SignUpCustomizedForm

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     template_name = "registration/signup.html"
#     success_url = "/"
class SignUpView(CreateView):
    form_class = SignUpCustomizedForm
    template_name = "registration/signup.html"
    success_url = "/"