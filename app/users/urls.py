from django.urls import path
from .views import user_registration, UserDetailsView

urlpatterns = [
    path('register/', user_registration, name='register'),
    path('user/', UserDetailsView.as_view(), name="user")
]
