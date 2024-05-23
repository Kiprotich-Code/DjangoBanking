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
            user_pin = form.cleaned_data['user_pin']
            user = authenticate(request, email=email, user_pin=user_pin, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    messages.success(request, ("Login Successful!"))
                    return redirect('dashboard')
                else:
                    messages.success(request, ("Login Successful!"))
                    return redirect('home')
                
            else:
                messages.warning(request, 'User Does Not Exists!')
                return redirect('login')
                
        else:
            messages.warning(request, 'Invalid Details! Enter the Correct details and try again!')

    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

# logout 
def user_logout(request):
    logout(request)
    return redirect('index')