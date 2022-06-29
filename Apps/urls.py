from django.urls import path
from .views import *

app_name = "Apps"

urlpatterns = [
    path("", HomveView.as_view(), name="index"),
    path("jregister/", JobseekerRegistrationView.as_view(), name="jregister"),
    path("eregister/", EmployerRegister.as_view(), name="eregister"),
    path("eindex/", EmployerIndex.as_view(), name="eindex"),
    path("jindex/", JobseekerIndex.as_view(), name="jindex"),
    path("postjob/", PostJobView.as_view(), name="postjob"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("singlejob/<int:pk>/",SingleJobView.as_view(),name="singlejob"),
    path("job/<int:pk>/apply/", JobApplyView.as_view(),name="apply"),
    # path("apply/<int:pk>/",ApplyView.as_view(),name="apply"),
    

    
    
]