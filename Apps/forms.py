from dataclasses import fields
from urllib import response
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
    logo = forms.ImageField(widget=forms.TextInput(attrs={'class':'form-group'}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    job_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    job_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    responsibilites = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    eduction_experiance = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    other_benifits = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))

    # published_on = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    vacancy = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-group'}))
    job_type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    experience = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-group'}))
    salary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    # deadline = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))

    class Meta:
        model = NewJob
        fields = ["logo","company_name","job_title","job_description","responsibilites","eduction_experiance","other_benifits","vacancy","job_type","location","experience","salary","gender"]

    # def 

#login form
class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username",'class':'form-group'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password",'class':'form-group'}))
    
class ApplicationForm(forms.ModelForm):
	class Meta:
		model=Application
		fields=["cv"]



   