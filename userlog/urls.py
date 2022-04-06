from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register', views.UserRegister, name="register"),
    path('', views.CustomerLogin.as_view(), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name="logout"),
    path('index', views.index, name="index")  
]
