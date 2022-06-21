from django.urls import path
from Apps import views

from .views import *

app_name = "Apps"

urlpatterns = [
    # path('', views.Index, name="index"),
    path("", HomveView.as_view(), name='home'),
    # path('register/', views.Register, name="register"),
    path("register/", RegistrationView.as_view(), name="register"),
    # path('login/', views.Login, name="login"),
    path("login/", LoginView.as_view(), name="login"),
]