from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
""" Registro de usuarios """
def user_registration(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect(to='/')
    else:
        form = UserRegisterForm()
            
    context = { 'form' : form }
    
    return render(request, 'registration/register.html', context)

def user_detail(request):
    return render(request, 'users/user_detail.html')
