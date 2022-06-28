from dataclasses import fields
from django import forms
from django.urls import re_path
from .models import*
from django.contrib.auth.models import User, Group
from django.forms import ModelForm

class EmployerForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    re_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # roll = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Employer
        fields = ["fullname","username","email","password","re_password","phone"]

    def groupadd(request):
        group = Group.objects.get(name="Employer")
        request.user.group.add(group)


    def clean_email(self):  #clean methhod used for validationerror
        email=self.cleaned_data["email"]
        if Employer.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already exist")
        return email

    def clean_username(self):  #clean methhod used for validationerror
        username=self.cleaned_data["username"]
        if Employer.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already exist")
        return username

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise forms.ValidationError("Password didnot match.")
        return re_password

class JoobseekerForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    re_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # roll = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Jobseeker
        fields = ["fullname","username","email","password","re_password","phone"]

    def clean_email(self):  #clean methhod used for validationerror
        email=self.cleaned_data["email"]
        if Jobseeker.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already exist")
        return email

    def clean_username(self):  #clean methhod used for validationerror
        username=self.cleaned_data["username"]
        if Jobseeker.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already exist")
        return username

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise forms.ValidationError("Password didnot match.")
        return re_password

class NewJobForm(forms.ModelForm):
    feature_img = forms.ImageField(widget=forms.TextInput(attrs={'class':'form-group'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-group'}))
    job_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    job_region = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    job_type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    job_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    tagline = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    company_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    website = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    facebook_username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    twitter_username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    linkedin_username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    logo = forms.ImageField(widget=forms.TextInput(attrs={'class':'form-group'}))

    class Meta:
        model = NewJob
        fields = ["feature_img","email","job_title","location","job_region","job_type","job_description","company_name","tagline","company_description","website","facebook_username","twitter_username","linkedin_username","logo"]

    # def 

#login form
class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username",'class':'form-group'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password",'class':'form-group'}))
    



   