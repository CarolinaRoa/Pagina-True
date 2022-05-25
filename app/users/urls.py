from django.urls import path
from .views import user_registration, UserDetailView, login_view


urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', login_view, name='login'),
    path('user/<str:username>/', UserDetailView.as_view(), name='user'),
]
