from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def user_reg(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

# logout 
def user_logout(request):
    logout(request)
    return redirect('index')