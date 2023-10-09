#from email import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
#from django.contrib.auth.model import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    context = {'form': form}
    
    return render(request, 'register.html',context=context)


def dashboard(request):
    return render(request, 'dashboard.html')


def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")

    return redirect('')


def account_locked(request):

    return render(request, 'account-locked.html')