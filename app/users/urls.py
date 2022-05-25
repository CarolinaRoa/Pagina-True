from django.urls import path
from .views import user_registration, user_detail
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('login/', LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('user/', user_detail, name='user'),
]
