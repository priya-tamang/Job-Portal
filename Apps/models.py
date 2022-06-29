from distutils.command.upload import upload
import email
from enum import auto
from mmap import mmap
from secrets import choice
from sqlite3 import Time
from django.db import models
from django.forms import PasswordInput
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse

# Create your models here.
class TimeStamp(models.Model):
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True

class Employer(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    re_password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        empgroup,created=Group.objects.get_or_create(name="Employer")
        self.user.groups.add(empgroup)
        super().save(*args, **kwargs)
        
        def __str__(self):
            return self.fullname


class Jobseeker(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    re_password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        group,created=Group.objects.get_or_create(name="JobSeeker")
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname

ROLL_CHOICE =(
    ( "Full Time","Full Time"),
    ("Part Time","Part Time" ),)

Gender =(
    ( "Male","Male"),
    ("Female","Female" ),
    ("Any","Any" ),
    )

class NewJob(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="media/")
    company_name = models.CharField(max_length=255, blank=True, null=True) 
    job_title = models.CharField(max_length=255, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    responsibilites = models.TextField(blank=True, null=True)
    eduction_experiance = models.TextField(blank=True, null=True)
    other_benifits = models.TextField(blank=True, null=True)

    # published_on = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=255, choices=ROLL_CHOICE)
    location = models.CharField(max_length=255, blank=True, null=True)
    experience = models.IntegerField(null=True, blank=True)
    salary = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255,null=True, blank=True, choices=Gender)
    # deadline = models.DateTimeField(y-m-d)
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.job_title

class Application(TimeStamp):
    job = models.ForeignKey(NewJob, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    cv = models.ImageField(upload_to="cv/")

    # def __str__(self):
    #     return self.job
