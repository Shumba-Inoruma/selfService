from django.urls import path
from .views import adminregisterUserCheck,loginadmin,dashboard,adminverify,allcooperates,cdmatomaswerasei,activates,deactivates

urlpatterns=[
    path('dashboard',dashboard,name='dashboard'),
    path('adminregisterUserCheck',adminregisterUserCheck,name="adminregisterUserCheck"),
    path('adminverify',adminverify,name="adminverify"),
    path('allcooperates',allcooperates,name="allcooperates"), 
    path('cdmatomaswerasei',cdmatomaswerasei,name="cdmatomaswerasei"),
    path('loginadmin', loginadmin,name="loginadmin"),
    path('activate/<slug:value>',activates,name="activate"),
    path('deactivate/<slug:value>',deactivates,name="deactivate"), 
  
    # path('sendemails',sendemailss,name="sendemailss")
    
]