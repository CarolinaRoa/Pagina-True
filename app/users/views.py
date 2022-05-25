from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/user_detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        #context["posts"] = Post.objects.filter(user=user).order_by('-created')
        
        
    

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

def login_view(request):
    if request.method=='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/user/'+username)
        else:
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')
