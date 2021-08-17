# from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CreateAccountForm, UserChangingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def home(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)

def SignUpView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        template_name = "registration/sign-up.html"
        form = CreateAccountForm()
        if request.method == "POST":
            form = CreateAccountForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
                
        context = {'form' : form}
        return render(request, template_name, context)

@login_required
def AccountView(request):
    template_name = "registration/account.html"
    form = UserChangingForm(instance=request.user)
    if request.method == "POST":
        form = UserChangingForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, template_name, context)
    

@login_required
def PasswordView(request):
    template_name = "registration/password.html"
    form = PasswordChangeForm(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account')
    context = {'form' : form}
    return render(request, template_name, context)
