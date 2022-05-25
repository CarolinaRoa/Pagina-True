from django.contrib import admin
from django.urls import path, include
from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    
    path('', include('users.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
