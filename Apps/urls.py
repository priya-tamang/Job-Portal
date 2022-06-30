from django.urls import path
from .views import *

app_name = "Apps"

urlpatterns = [
    path("", HomveView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("eabout/", EmpolyerAboutView.as_view(), name="eabout"),
    path("jabout/", JobseekerAboutView.as_view(), name="jabout"),
    path("econtact/", EmployerContactView.as_view(), name="econtact"),
    path("jcontact/", JobseekerContactView.as_view(), name="jcontact"),
    path("jregister/", JobseekerRegistrationView.as_view(), name="jregister"),
    path("eregister/", EmployerRegister.as_view(), name="eregister"),
    path("eindex/", EmployerIndex.as_view(), name="eindex"),
    path("jindex/", JobseekerIndex.as_view(), name="jindex"),
    path("postjob/", PostJobView.as_view(), name="postjob"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("singlejob/<int:pk>/",SingleJobView.as_view(),name="singlejob"),
    path("job/<int:pk>/apply/", JobApplyView.as_view(),name="apply"),
    path("search/", JobSearchView.as_view(),name="search"),
    path("empsinglejob/<int:pk>/", EmpSingleJobView.as_view(),name="empsinglejob"),
    path("jsinglejob/<int:pk>/", JobseekerSingleJobView.as_view(),name="jsinglejob"),
    

    
    
]