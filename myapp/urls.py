from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('create-account/', views.SignUpView, name="create-account"),
    path('account/', views.AccountView, name="account"),
    path('password/', views.PasswordView, name="password"),
]
