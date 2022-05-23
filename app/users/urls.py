from django.urls import path
from .views import user_registration, user_profile

urlpatterns = [
    path('register/', user_registration, name='register'),
    path('userprofile/', user_profile, name='userprofile')
]
