
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('selfServiceApp.urls')),
    path("adminuser/", include('adminuser.urls')),
   
]
