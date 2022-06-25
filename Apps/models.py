import email
from secrets import choice
from django.db import models
from django.forms import PasswordInput
from django.db import models
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse

# Create your models here.
class TimeStamp(models.Model):
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True

ROLL_CHOICE =(
    ("1", "Employer"),
    ("2", "Jobseeker"),)

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    re_password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fullname


class Jobseeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    re_password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fullname

ROLL_CHOICE =(
    ( "Full Time","Full Time"),
    ("Part Time","Part Time" ),)

class NewJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_img = models.ImageField(upload_to='')
    email = models.EmailField(max_length=255, blank=True, null=True)   
    job_title = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    job_region = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=255, choices=ROLL_CHOICE)
    job_description = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True) 
    tagline = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    facebook_username = models.CharField(max_length=255, blank=True, null=True)
    twitter_username = models.CharField(max_length=255, blank=True, null=True)
    linkedin_username = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email