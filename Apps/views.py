from collections import UserList
from operator import ge
from pipes import Template
from re import T
from tokenize import group
from urllib import request
from venv import create
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView , CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# import urllib.request
from .forms import*
from django.contrib import messages 


class EmployerRegister(generic.CreateView):
    form_class = EmployerForm
    template_name = "Auth/Eregister.html"
    success_url = reverse_lazy("Auth/login")
    def post(self,request):
        form = EmployerForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            phone = form.cleaned_data['phone']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            employer = Employer.objects.create(user=user,username=username, fullname=fullname, email=email,password=password, phone=phone)
            employer.save()
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse("errors")


class HomveView(TemplateView):
    template_name = "Home/index.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        new = NewJob.objects.all().order_by("-id")
        context = {"newjob":new}
        return context

class JobseekerRegistrationView(TemplateView):
    template_name = "Auth/Jregister.html"
    form_class = JoobseekerForm
    success_url = "/"
    def post(self, request):
        form = JoobseekerForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            phone = form.cleaned_data['phone']
            user = User.objects.create_user(username=username, email=email,password=password)
            user.save()
            jobseeker = Jobseeker.objects.create(user=user,username=username, fullname=fullname, email=email,password=password, phone=phone)
            jobseeker.save()
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse("errors")
            
class EmployerIndex(generic.CreateView):
    template_name = "Emp/employerhome.html"
    form_class = NewJobForm
    success_url = "/"

class JobseekerIndex(generic.CreateView):
    template_name = "Jobseeker/jobseeker.html"
    form_class = NewJobForm
    success_url = "/"
   
class PostJobView(generic.CreateView):
    template_name = "Home/postjob.html"
    form_class = NewJobForm
    success_url = "/"

    def post(self, request):
        # print("data from post of a job",request.POST)
        form = NewJobForm(request.POST,request.FILES)
        # print("cleaned data", newform.cleaned_data)
        # print(request.POST.get('feature_img'))
        # print(request.POST.get('email'))
        # print(request.POST.get('job_title'))
        # print(request.POST.get('twitter_username'))
        # print(request.POST.get('logo'))
        # if form.is_valid():
        user = request.user
        feature_img =request.FILES.get('feature_img')
        email = request.POST.get('email')
        job_title = request.POST.get('job_title')
        location = request.POST.get('location')
        job_region = request.POST.get('job_region')
        job_type = request.POST.get('job_type')
        job_description = request.POST.get('job_description')
        company_name = request.POST.get('company_name')
        tagline = request.POST.get('tagline')
        company_description = request.POST.get('company_description')
        website = request.POST.get('website')
        facebook_username = request.POST.get('facebook_username')
        twitter_username = request.POST.get('twitter_username')
        linkedin_username = request.POST.get('linkedin_username')
        logo = request.FILES.get('logo')
        print(logo, 555555555555555555555555555555)
        form = NewJob.objects.create(user = user,feature_img=feature_img, email=email, job_title=job_title,location=location, job_region=job_region, job_type=job_type,job_description=job_description,company_name=company_name,tagline=tagline,company_description=company_description, website=website, facebook_username=facebook_username, twitter_username=twitter_username, linkedin_username=linkedin_username, logo=logo)
        form.save()
        return HttpResponseRedirect('/')

# class BaseMixin(object):  #BaseMixin afai ma view haina tara yesko property arko class ma inherite garana sakinxa
# 	def get_context_data(self,**kwargs):     #html ma View bata data pathauna get_context_data use garinxa
# 		context=super().get_context_data(**kwargs)
    
class LoginView(FormView):
    template_name = "Auth/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
        else:
            return render("error")

        return super().form_valid(form)
    
    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name="Employer").exists():
            return "/eindex/"
        elif user.groups.filter(name="Jobseeker").exists():
            return "/jobindex/"
        elif user.groups.filter(name="Admin").exists():
            return "/Admin/"
        else:
            return "/login/"
            

    # def form_valid(self,form):
    #     username =form.cleaned_data['username']
    #     password =form.cleaned_data['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #     else:
    #         return HttpResponse("errors")

    #     return super().form_valid(form)
    
    # def get_success_url(self):
    #     user=self.request.user
    #     if user.groups.filter(name="Employer").exists():
    #         return HttpResponseRedirect("/eindex/")
    #     elif user.groups.filter(name="Jobseeker").exists():
    #         return HttpResponseRedirect("/jindex/")
    #     else:
    #         return HttpResponse("error")


    # def post(self, request):
    #     form = self.form_class(data = request.POST)
    #     username =request.POST['username']
    #     password =request.POST['password']
    #     # print("form datas", form.data)
    #     # print("validation", form.is_valid())
    #     # print("data after clean", form.cleaned_data)
    #     if form.is_valid():
    #         # print("inside is valid")
    #         user = authenticate(request, username=username, password=password)
    #         print(username)
    #         if user is not None:
    #             login(request, user)
    #             messages.success(request, ('You Have Been Logged In!'))
    #             return HttpResponseRedirect('/')

    #         else:
    #             messages.success(request, ('Error Logging In - Please Try Again...'))
    #             return HttpResponseRedirect('login')

    #     return super().form_valid(form)
    # def get_success_url(self):
    #     user=self.request.user
    #     if user.groups.filter(name="Employer").exists():
    #         return HttpResponseRedirect("/eindex/")

    #     elif user.groups.filter(name="Jobseeker").exists():
    #         return HttpResponseRedirect("/jindex/")

    #     else:
            # return "/login"



    

class LogoutView(TemplateView):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect("/")

    
      



    



