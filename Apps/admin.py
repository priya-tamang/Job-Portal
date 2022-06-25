from django.contrib import admin
from Apps.models import Employer, Jobseeker, NewJob
# Register your models here.
@admin.register(Employer)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username','fullname','email','phone']

@admin.register(Jobseeker)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username','fullname','email','phone']

@admin.register(NewJob)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['user','email','job_title','company_name']



