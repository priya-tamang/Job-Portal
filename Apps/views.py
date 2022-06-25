from collections import UserList
from operator import ge
from pipes import Template
import re
from tokenize import group
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate,login,logout
# import urllib.request
import urllib.request as ur
from .forms import*
from django.contrib import messages 


# Create your views here.
# class EmployeeRegistrationView(TemplateView):
#     template_name = "Auth/Eregister.html"
#     form_class = EmployerForm
#     success_url = "/"
#     def post(self,request):
#         form = EmployerForm(request.POST)
#         if form.is_valid():
#             fullname = form.cleaned_data['fullname']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             re_password = form.cleaned_data['re_password']
#             phone = form.cleaned_data['phone']
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.save()
#             employer = Employer.objects.create(user=user,username=username, fullname=fullname, email=email,password=password, phone=phone)
#             employer.save()
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponse("errors")

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
        job = NewJobForm()
        new = NewJob.objects.all()
        context = {"job":job, "newjob":new}
        return context

# class JobseekerRegistrationView(TemplateView):
#     template_name = "Auth/Jregister.html"
#     form_class = JoobseekerForm
#     success_url = "/"
#     def post(self, request):
#         form = JoobseekerForm(request.POST)
#         if form.is_valid():
#             fullname = form.cleaned_data['fullname']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             re_password = form.cleaned_data['re_password']
#             phone = form.cleaned_data['phone']
#             user = User.objects.create_user(username=username, email=email,password=password)
#             user.save()
#             jobseeker = Jobseeker.objects.create(user=user,username=username, fullname=fullname, email=email,password=password, phone=phone)
#             jobseeker.save()
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponse("errors")
            

   
# class PostJobView(TemplateView):
#     template_name = "Home/postjob.html"
#     form_class = NewJobForm
#     success_url = "/"
#     def post(self, request):
#         newform = NewJobForm(request.POST)
#         if newform.is_valid():
#             feature_img = newform.cleaned_data['feature_img']
#             email = newform.cleaned_data['email']
#             job_title = newform.cleaned_data['job_title']
#             location = newform.cleaned_data['location']
#             job_region = newform.cleaned_data['job_region']
#             job_type = newform.cleaned_data['job_type']
#             job_description = newform.cleaned_data['job_description']
#             company_name = newform.cleaned_data['company_name']
#             tagline = newform.cleaned_data['tagline']
#             company_description = newform.cleaned_data['company_description']
#             website = newform.cleaned_data['website']
#             facebook_username = newform.cleaned_data['facebook_username']
#             twitter_username = newform.cleaned_data['twitter_username']
#             linkedin_username = newform.cleaned_data['linkedin_username']
#             logo = newform.cleaned_data['logo']
#             newjob = User(feature_img=feature_img, email=email, job_title=job_title,location=location, job_region=job_region, job_type=job_type,job_description=job_description,company_name=company_name,tagline=tagline,company_description=company_description, website=website, facebook_username=facebook_username, twitter_username=twitter_username, linkedin_username=linkedin_username, logo=logo)
#             newjob.save()
#             print(f"new job : {newjob}")
#             return HttpResponseRedirect('/')

    
class LoginView(TemplateView):
    template_name = "Auth/login.html"
    form_class = LoginForm
    success_url = "/"

    def post(self, request):
        form = self.form_class(data = request.POST)
        username =request.POST['username']
        print(username)
        password =request.POST['password']
        if form.is_valid():
            print("inside is valid")
            user = authenticate(request, username=username, password=password)
            print(username)
            if user is not None:
                login(request, user)
                messages.success(request, ('You Have Been Logged In!'))
                return HttpResponseRedirect('/')

            else:
                messages.success(request, ('Error Logging In - Please Try Again...'))
                return HttpResponseRedirect('login')
        else:
            return HttpResponse("errors")
        



        #         username =form.cleaned_data['username'],
        #         print(username)
        #         password =form.cleaned_data['password']
        #         try:
        #             user = authenticate(username=username, password=password)
        #             print(f"Hello,{user}")
        #             return HttpResponseRedirect("/")
        #         except:
        #             return HttpResponse("Invalid username or password")
        # else:
        #     return HttpResponse("errors")
    
      



    



