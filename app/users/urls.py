from django.urls import path
from .views import user_registration, UserDetailsView, login_view

urlpatterns = [
    path('register/', user_registration, name='register'),
    path('user/', UserDetailsView.as_view(), name="user"),
    path('login/', login_view, name='login')
]
