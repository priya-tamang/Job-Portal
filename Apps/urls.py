from django.urls import path
from Apps import views

from .views import *

app_name = "Apps"

urlpatterns = [
    path("", HomveView.as_view(), name="index"),
    # path("jregister/", JobseekerRegistrationView.as_view(), name="jregister"),
    path("eregister/", EmployerRegister.as_view(), name="eregister"),
    path("postjob/", PostJobView.as_view(), name="postjob"),
    path("login/", LoginView.as_view(), name="login"),
    
]