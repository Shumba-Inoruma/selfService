from django.shortcuts import render,HttpResponse,redirect
import grpc
from . import payments_pb2
from . import payments_pb2_grpc
from . import users_pb2
from . import users_pb2_grpc
import logging
import requests
from itertools import chain
from django.views.decorators.csrf import csrf_exempt
import re
import time
from .forms import registerForm,registerFormCooperate,verifyForm,captcha,loginForm,cooperatestep2Form,contactForm
import random
from selfServiceApp.models import users,cooperates
from django.contrib import messages
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
import http.client
from django.core import serializers
from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.http import FileResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import re




from django.shortcuts import render


@login_required(login_url='/adminuser/loginadmin')
def dashboard(request):
        
        if 'realadmin' in request.session:

    # try:
            context={'allusers':reversed(users.objects.all()),'count':users.objects.all().count()}
            return render(request,'dashboard.html',context)
        # except:
        #      return HttpResponse("none recordss")

        else:
             return redirect('loginadmin')



@login_required(login_url='/adminuser/loginadmin')
def cdmatomaswerasei(request):
        
        if 'realadmin' in request.session:

        # try:
            context={'allusers':reversed(users.objects.all()),'count':users.objects.all().count()}
            return render(request,'admin.html',context)
        # except:
        #      return HttpResponse("none recordss") 
        else:
            return redirect('loginadmin')   
@login_required(login_url='/adminuser/loginadmin')
def allcooperates(request):
         
        if 'realadmin' in request.session:

            # try:
                context={'allcooperates':reversed(cooperates.objects.all()),'count':cooperates.objects.all().count()}
                return render(request,'allcooperates.html',context)
            # except:
            #      return HttpResponse("none recordss")

        else:
            return redirect('loginadmin')   


@login_required(login_url='/adminuser/loginadmin')
def adminregisterUserCheck(request):   
    if 'realadmin' in request.session:
        form=registerForm()
        form2=verifyForm()   
        if request.method=="POST":
            form=registerForm(request.POST)
            if form.is_valid():
                  
                    if True:
                    
                        user=users()
                        user.email=form.cleaned_data.get('email')
                        user.gsmnumber=form.cleaned_data.get('gsmnumber')
                        user.password=form.cleaned_data.get('password')
                        user.cdmanumber=request.POST['cdmanumber']
                        user.save()
                        
                    
                        if True:
                            realuser = User.objects.create_user(form.cleaned_data.get('gsmnumber'), form.cleaned_data.get('email'), form.cleaned_data.get('password'))
                            realuser.save()

                        # resp=testVerification(form.cleaned_data.get('gsmnumber'))
                        resp=1
                        if resp==1:
                            number={'numbers':request.POST['gsmnumber'],'res':resp,"form2":form2,'password':request.POST['password'],'message':"Please enter the verification code we just sent to: "+request.POST['gsmnumber'],"cdmanumber":request.POST['cdmanumber']}
                            return render(request,'adminverify.html',number)
                        elif resp==3:
                            messages.info(request,resp.error.localizedDescription)
                            con = {
                            "form": registerForm(request.POST),
                            'captch':captcha()
                        }
                            number={'numbers':request.POST['gsmnumber'],'res':resp,"form2":form2,'password':request.POST['password'],"message":resp.error.localizedDescription,"cdmanumber":request.POST['cdmanumber']}
                            return render(request,'pages-register.html',con)
                        
                        else:
                            messages.info(request,resp.error.localizedDescription)
                            con = {
                            "form": registerForm(request.POST),
                            'captch':captcha()
                        }
                            return render(request,'pages-register.html',con)
                    else:
                        con = {
                            "form": registerForm(request.POST),
                            'captch':captcha(request.POST)
                        }
                        return render(request,'pages-register.html',con)
            else:
                messagee=[]
                request.session['email']=''
                request.session['cdmanumber']=''
                request.session['gsmnumber']=''

                    
                 
                request.session['email']=request.POST['email'] 
                request.session['cdmanumber']=request.POST['cdmanumber']
                request.session['gsmnumber']=request.POST['gsmnumber']

                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                messages.success(request,"Errors Found: Please make sure all fields are filled correctly")
                if users.objects.filter(email=request.POST['email']).exists()  or cooperates.objects.filter(email=request.POST['email']).exists():
                    messages.success(request,"Email Taken")
                elif re.fullmatch(regex, request.POST['email'])==None and request.POST['email']!="":
                    messages.success(request,"Incorrect Email")
                if(request.POST['password']!=request.POST['confirmpassword']):
                    messages.success(request,"Passwords Did Not Match")
                elif len(request.POST['password'])<3 and len(request.POST['password'])>0 :
                    messages.success(request,"Password must be atleast 3 characters")

                if users.objects.filter(gsmnumber=request.POST['gsmnumber']).exists():
                    messages.success(request,"Gsm Number Taken")
                if users.objects.filter(cdmanumber=request.POST['cdmanumber']).exists() and request.POST['cdmanumber']!="":
                    messages.success(request,"Cdma Number Taken")    
                con = {
                    "form": registerForm(request.POST),
                    'captch':captcha(request.POST)
                }
                return redirect("cdmatomaswerasei")
        else:
            con = {
            "form": registerForm(None) ,
            'captcha':captcha()
                }
            return render(request,'pages-register.html',con)
    else:
            
        return redirect('loginadmin')   
@login_required(login_url='/adminuser/loginadmin')
def registerUser(request):
    if 'realadmin' in request.session:
          return render(request,'pages-register.html')
    else:
          return redirect('loaginadmin')


@login_required(login_url='/adminuser/loginadmin')
def registerCdma(username,verificationCode,cdmanumber,password):
    if 'realadmin' in request.session:
        with grpc.insecure_channel('talk.ai.co.zw:50000') as channel:
            stub = users_pb2_grpc.userServiceStub(channel)
            information=users_pb2.request(username=username, cdma=cdmanumber,password=password,domain='localvoip.ai.co.zw',verificationCode=verificationCode)
            response=stub.RegisterCDMA(information)
        return response 
    else:
          return redirect('adminlogin')

@login_required(login_url='/adminuser/loginadmin')
def adminverify(request):
     
    if 'realadmin' in request.session:
        form2=verifyForm()
        try:
            if request.method=="POST":
                resp= registerCdma(request.POST['number'],request.POST['verificationcode'],request.POST['cdmanumber'],request.POST['password'])
                print(resp.status)
                print(resp)
                print(resp.error.localizedDescription)
                if resp.status==1:
                    user=users.objects.get(gsmnumber=request.POST['number'])
                    user.registered=True
                    user.alliasNumber=resp.alias
                    user.save()
                    request.session['activeuser']=request.POST['number']
                    user=users.objects.get(gsmnumber=request.session['activeuser'])
                    cont={'user':request.session['activeuser']}
                    messages.success(request,"Number Converted Successfully!")
                    return render(request,'admin.html',cont)

                else:
                    messages.info(request,"Verification Failed, Please Try Again!")
                    number={'numbers':request.POST['number'],'res':resp,"form2":form2,'password':request.POST['password']}
                    return render(request,'verify.html',number)

        except:
            return HttpResponse("Network Error")
    else:
         return redirect('loginadmin')

@login_required(login_url='/adminuser/loginadmin')
def activates(request,value):
    if 'realadmin' in request.session:

        user=users.objects.get(gsmnumber=value)
        user.registered=True
        user.save()
        return redirect('dashboard')  
    else:
         return redirect('loginadmin')

@login_required(login_url='/adminuser/loginadmin')
def deactivates(request,value):
    if 'realadmin' in request.session:
 
        user=users.objects.get(gsmnumber=value)
        user.registered=False
        user.save()
        return redirect('dashboard') 
    else:
         return redirect('loginadmin')


  

def loginadmin(request):

    request.session.flush()
    logout(request)
    
    if request.method=="POST":
                        try:
                                if users.objects.get(gsmnumber=request.POST['email'],password=request.POST['password']):
                                    user = authenticate(request, username='password', password='password')
                                    if users is not None:
                                        user = User.objects.get(username='password')
                                        login(request, user) 
                                        if request.POST['email']=="password" and request.POST['password']=="password":
                                            request.session['realadmin']="True"
                                            return redirect('dashboard')
                                        else:
                                            return redirect('login')
                                    
                                    else:
                                        messages.info(request,"username or password incorrect")
                                        return redirect('login')   

                                else:
                                    messages.info(request,"username or password incorrect")
                                    return render(request,'adminlogin.html') 
                        except:
                               messages.info(request,"username or password incorrect")
                               return render(request,'adminlogin.html')    
      
    return render(request,'adminlogin.html') 





 
  


  


