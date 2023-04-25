from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,checkBalance,rechargeAccount,paynow,voucher,cooperatestep2,registerUser,loginuser,registerCooperate,testVerification,verify,checkCoperate,registerUserCheck,loginuser,profile,sendmail,approveCoperate,downloadcr14,downloadcr6,downloadproofofresidence,downloadrepresantativeid,approved,registerCoperateCheck,verifybusiness,signout,contact,customerMail,faqs,choose,finishregistering




urlpatterns=[
    path('',home,name="home"),
    path('checkBalance',checkBalance,name="checkBalance"),
    path('rechargeAccount',rechargeAccount,name="recharge"),
    # path("test",testVerification,name="verify"),
    path('registeruser',registerUser,name="registeruser"),
    path('registercooperate',registerCooperate,name='registercooperate'),
    path('re',testVerification,name='re'),
    path('verify',verify,name='verify'),
    path('checkCoperate',checkCoperate,name='checkCoperate'),
    path("registerUserCheck",registerUserCheck,name="registerUserCheck"),
    path('testVerification', testVerification,name="testVerification"),
    path('loginuser',loginuser,name="loginuser"),
    path('profile',profile,name="profile"), 
    path('sendmail',sendmail,name="sendmail"),
    path('approveCoperate',approveCoperate,name="approveCoperate"),
    path('downloadcr6/<str:name>',downloadcr6,name="downloadcr6"),
    path('downloadcr14/<str:name>',downloadcr14,name="downloadcr14"),
    path('downloadproofofresidence/<str:name>',downloadproofofresidence,name="downloadproofofresidence"),
    path('downloadrepresantativeid/<str:name>',downloadrepresantativeid,name="downloadrepresantativeid"),
    path('approved/<str:name>',approved,name="approved"),
    path('cooperatestep2/<str:name>',cooperatestep2,name="cooperatestep2"),
    path("registerCoperateCheck",registerCoperateCheck,name="registerCoperateCheck"),
    path('verifybusiness',verifybusiness,name='verifybusiness'),
    path('signout',signout,name="signout"),
    path('contact',contact,name="contact"),
    path('customerMail',customerMail,name="customerMail"),
    path('faqs',faqs,name="faqs"),
    path('choose',choose,name="choose"),
    path('finishregistering',finishregistering,name="finishregistering"),
    path('paynow',paynow,name='paynow'),
    path('voucher',voucher,name='voucher')
   
    





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)