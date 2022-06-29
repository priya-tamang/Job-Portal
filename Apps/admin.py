from django.contrib import admin
from Apps.models import Employer, Jobseeker, NewJob, Application
# Register your models here.
@admin.register(Employer)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username','fullname','email','phone']

@admin.register(Jobseeker)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username','fullname','email','phone']

@admin.register(NewJob)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['user','job_title']

@admin.register(Application)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['job', 'jobseeker']



