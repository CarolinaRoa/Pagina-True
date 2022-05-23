from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import UserProfile

# Create your views here.
""" Registro de usuarios """
def user_registration(request):
    data = {
        'form': CustomUserCreationForm()
    }
    print("hola")
    
    if request.method == 'POST':
        print("estoy dentro de post")
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
            login(request, user)
            print("Sisas")
            
            
            """Redirect to home"""
            return redirect(to="/")
            
            
        data["form"] = form
        
        
        
    return render(request, 'registration/register.html', data)
