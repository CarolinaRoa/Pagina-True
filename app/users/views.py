from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
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
                user_name = form.cleaned_data["user_name"],
                password = form.cleaned_data["password"]
            )
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print("Sisas")
            
            
            """Redirect to home"""
            return redirect(to="/")
            
            
        data["form"] = form
        
        
        
    return render(request, 'registration/register.html', data)

"""def user_detail(request):
    
    context = {
        user_name: UserProfile.object.get(user_name)
    }
    
    return render(request, 'users/user_detail.html', context)"""
    
    
class UserDetailsView(ListView):
    template_name = 'users/user_detail.html'
    model = UserProfile
    ordering = ('-created')
    context_object_name = 'users'
    
def login_view(request):
    """Login view."""
    print("Bebecita prr")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            print("Coronamo perros")
            login(request, user)
            return redirect('users/user_detail.html')
        else:
            print("pailas")
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'registration/login.html')
    
    