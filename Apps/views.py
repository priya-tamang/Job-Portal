from calendar import c
from collections import UserList
from multiprocessing import get_context
from operator import ge
from pipes import Template
from re import T, sub, template
from tokenize import group
from unittest import result
from urllib import request
from venv import create
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import TemplateView , CreateView, FormView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import urllib.request
from .forms import *
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from django.db.models import Q # search ma or logic lagauna lai import gareko

class EmployerRequiredMixin(object):
	def dispatch(self,request,*args,**kwargs):       #dispatch fuction is used for only private login  
		user=request.user
		if user.is_authenticated and user.groups.filter(name="Employer").exists():
			pass
		else:
			return redirect("/login/")


		return super().dispatch(request,*args,**kwargs)

class JobSeekerRequiredMixin(object):
	def dispatch(self,request,*args,**kwargs):
		user=request.user
		if user.is_authenticated and user.groups.filter(name="JobSeeker").exists():
			pass
		else:
			return redirect("/login/")

		return super().dispatch(request,*args,**kwargs)


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

class JobseekerRegistrationView(generic.CreateView):
    form_class = JoobseekerForm
    template_name = "Auth/Jregister.html"
    success_url = reverse_lazy("Auth/login")
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

class HomveView(TemplateView):
    template_name = "Home/index.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        new = NewJob.objects.all().order_by("-id")
        candidatescount = Jobseeker.objects.all().count()
        candidatescount = str(candidatescount)

        context = {
            "newjob":new, 
            "count":candidatescount
            }
        return context
            
class EmployerIndex(EmployerRequiredMixin,generic.TemplateView):
    template_name = "Emp/employerhome.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        new = NewJob.objects.all().order_by("-id")
        context = {"newjob":new}
        return context

class JobseekerIndex(JobSeekerRequiredMixin, generic.TemplateView):
    template_name = "Jobseeker/jobseeker.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        new = NewJob.objects.all().order_by("-id")
        context = {"newjob":new}
        return context
   
class PostJobView(LoginRequiredMixin, EmployerRequiredMixin, generic.CreateView):
    template_name = "Home/postjob.html"
    form_class = NewJobForm
    success_url = "/eindex/"
    
    def post(self, request):
        form = NewJobForm(request.POST,request.FILES)
        user = request.user
        logo =request.FILES.get('logo')
        company_name = request.POST.get('company_name')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        responsibilites = request.POST.get('responsibilites')
        eduction_experiance = request.POST.get('eduction_experiance')
        other_benifits = request.POST.get('other_benifits')

        # published_on = request.POST.get('published_on')
        vacancy = request.POST.get('vacancy')
        job_type = request.POST.get('job_type')
        location = request.POST.get('location')
        experience = request.POST.get('experience')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        gender = request.POST.get('gender')
        # deadline = request.FILES.get('deadline')

        form = NewJob.objects.create(user = user, logo=logo, company_name=company_name,job_title=job_title, job_description=job_description, responsibilites=responsibilites, eduction_experiance=eduction_experiance, other_benifits=other_benifits,vacancy=vacancy, job_type=job_type, location=location, experience=experience, salary=salary, gender=gender)
        form.save()
        return HttpResponseRedirect('/eindex/')
    
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
            return "/error/"

        return super().form_valid(form)
    
    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name="Employer").exists():
            return "/eindex/"
        elif user.groups.filter(name="JobSeeker").exists():
            return "/jindex/"
        elif user.groups.filter(name="Admin").exists():
            return "/Admin/"
        else:
            return "/login/"


class LogoutView(TemplateView):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect("/")

class SingleJobView(TemplateView):
    template_name = "singlejob.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # new = NewJob.objects.all()
        # context = {"newjob":new}

        NewJob_id=self.kwargs['pk']
        job = NewJob.objects.get(pk=NewJob_id)
        job.view_count = 1
        job.save()
        context = {"job": job}

        return context

class EmpSingleJobView(TemplateView):
    template_name = "Emp/esinglejob.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        NewJob_id=self.kwargs['pk']
        job = NewJob.objects.get(pk=NewJob_id)
        job.view_count = 1
        job.save()
        job.save()
        context = {"job": job}

        return context

class JobseekerSingleJobView(TemplateView):
    template_name = "Jobseeker/jsinglejob.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        NewJob_id=self.kwargs['pk']
        job = NewJob.objects.get(pk=NewJob_id)
        job.view_count = 1
        job.save()
        job.save()
        context = {"job": job}

        return context


class JobApplyView(JobSeekerRequiredMixin,CreateView):
    template_name = "Jobseeker/apply.html"
    form_class = ApplicationForm
    success_url = "/jindex/"

    def form_valid(self,form):
        job_id=self.kwargs["pk"]  #job ko id lai liyeko from urls
        job=NewJob.objects.get(id=job_id) #model batw job liyeko jasko id chai job_id x jun chai hamile name diyeko 
        form.instance.job=job  #form vaneko form_class ma vayeko form jun chai application form ra instance vaenko 
                                
        loggedin_user=self.request.user 
        jobseeker=Jobseeker.objects.get(user=loggedin_user) #jobseeker model ma vayeko user vaneko loggedin user nai ho 
        form.instance.jobseeker=jobseeker

        message = jobseeker.fullname + " applied on your " + job.job_title + " job "
        send_mail(
            "Some one applied your job", 
            message,
            settings.EMAIL_HOST_USER,
            [job.user.email, "priyatamang@cagtu.com"],
            fail_silently=False
        )
        send_mail(
            "Successfully applied", 
            "You have successfully applied for the job",
            settings.EMAIL_HOST_USER,
            [jobseeker.email],
            fail_silently=False
        )

        return super().form_valid(form)

class JobSearchView(TemplateView):
    template_name = "Home/search.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        kw = self.request.GET['search']
    
        results = NewJob.objects.filter(Q(job_title__icontains=kw)|
                                        Q(location__icontains=kw)|
                                        Q(job_type__icontains=kw)
                                        )
        context['search_results'] = results
        print(context, "fffffffffffffffffffffffffffffffffff")
        return context

class AboutView(TemplateView):
    template_name = "Home/about.html"

class EmpolyerAboutView(TemplateView):
    template_name = "Emp/allabout.html"

class JobseekerAboutView(TemplateView):
    template_name = "Jobseeker/jabout.html"



class ContactView(generic.CreateView):
    template_name = "Home/contact.html"
    # model = Contact
    form_class = ContactForm
    success_url ="/"

    def post(self, request):
        # form = ContactForm(request.POST)
        firstname = request.POST.get('firstname')
        print(firstname)
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')   
        message = request.POST.get('message')
        form = Contact.objects.create( firstname=firstname,lastname=lastname, email=email, subject=subject, message=message)

        
        subject = "Contact Form Filled by:" + firstname + " " + lastname
        message = "Hello Admin, Here are the contact form details.\n\nname:" + firstname +"\nemail:" + email + "\nmessage:" + message
        from_email = settings.EMAIL_HOST_USER
        to_list = ["priyatamang565@gmail.com"]
        send_mail(subject, message, from_email, to_list)
        messages.info(request, 'Thank you  we will contact you shortly!!!')
        return HttpResponseRedirect("/contact/")
   

        




class EmployerContactView(TemplateView):
    template_name = "Emp/allcontact.html"
    form_class = ContactForm
    success_url ="/"
    

class JobseekerContactView(TemplateView):
    template_name = "Jobseeker/jcontact.html"
    form_class = ContactForm
    success_url ="/"






        







