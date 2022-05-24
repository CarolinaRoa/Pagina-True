from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.
""" Registro de usuarios """
def user_registration(request):
    
    data = {
        'form': CustomUserCreationForm()
    }
    print("hola")
    
    if request.method == 'POST':
        display_type = request.POST.get("display_type", None)
        if display_type in ["locationbox", "displaybox"]:
            print("estoy dentro de post")
            form = CustomUserCreationForm(data=request.POST)
        
            if form.is_valid():
                form.save()
                user = authenticate(
                    user_name = form.cleaned_data["user_name"],
                    password = form.cleaned_data["password"]
                )
                login(request, user)
                #messages.warning(request, 'Your account expires in three days.')
            
            
                """Redirect to home"""
                return redirect(to="/")
            
            
            data["form"] = form
        else:
            messages.warning(request, 'Your account expires in three days.')
        
    return render(request, 'registration/register.html', data)


"""class UserListView(TemplateView):
    template_name = 'users/userprofile.html'
    
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context.update(user=self.request.user)
        return context"""
    
    

def user_profile(request):
    queryset = UserProfile.objects.get(
        user_name,
        email
    )
    context = {'queryset':queryset}
    return render(request, 'users/userprofile_list.html', context)

