from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
# def Index(request):
#     return render(request, 'Home/index.html')

class HomveView(TemplateView):
    template_name = "Home/index.html"


# def Register(request):
#     return render(request, 'Auth/register.html')

class RegistrationView(TemplateView):
    template_name = "Auth/register.html"

# def Login(request):
#     return render(request, 'Auth/login.html')

class LoginView(TemplateView):
    template_name = "Auth/login.html"

