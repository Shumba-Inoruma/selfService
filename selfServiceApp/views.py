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
from .models import users,cooperates
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
from paynow import Paynow
from multiprocessing import Process
import requests


def sendmail(subject,message,email):

        send_mail(
            subject,
            message,
            'chirovemunyaradzi@gmail.com',
            email,
            fail_silently=False,
        )
        return HttpResponse(send_mail)

# @login_required(login_url='/loginuser')
def home(request):
    # if users.objects.filter(gsmnumber=request.session['activeuser']).exists():
    #     user=request.session['activeuser']
    #     cont={'user':user}
    #     return render(request,'index.html',cont)  
    # else:
    #     user=cooperates.objects.get(gsmnumber=request.session['activeuser'])
    #     user=request.session['activeuser']
    #     cont={'user':user}
        return render(request,'index.html')
def loginuser(request):

    return render(request,'pages-login.html')

def verify(request):
    form2=verifyForm()
    if request.method=="POST":
        resp= register(request.POST['number'],request.POST['verificationcode'],request.POST['password'])

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
            return render(request,'index.html',cont)

        else:
            messages.info(request,"Verification Failed, Please Try Again!")
            number={'numbers':request.POST['number'],'res':resp,"form2":form2,'password':request.POST['password']}
            return render(request,'verify.html',number)
        

 
def registerUserCheck(request):
      

   
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
                    user.save()
                   
                    if True:
                        realuser = User.objects.create_user(form.cleaned_data.get('gsmnumber'), form.cleaned_data.get('email'), form.cleaned_data.get('password'))
                        realuser.save()

                    resp=testVerification(form.cleaned_data.get('gsmnumber'))
                   
                    if resp.status==1:
                        number={'numbers':request.POST['gsmnumber'],'res':resp,"form2":form2,'password':request.POST['password'],'message':"Please enter the verification code we just sent to: "+request.POST['gsmnumber']}
                        return render(request,'verify.html',number)
                    elif resp==3:
                        messages.info(request,resp.error.localizedDescription)
                        con = {
                        "form": registerForm(request.POST),
                        'captch':captcha()
                    }
                        number={'numbers':request.POST['gsmnumber'],'res':resp,"form2":form2,'password':request.POST['password'],"message":resp.error.localizedDescription}
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
                   
            request.session.flush()
            request.session['email']=request.POST['email'] 
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
           
            con = {
                "form": registerForm(request.POST),
                'captch':captcha(request.POST)
            }
            return redirect("registerUserCheck")
    else:
        con = {
        "form": registerForm(None) ,
        'captcha':captcha()
            }
        return render(request,'pages-register.html',con)

def registerUser(request):
 
    return render(request,'pages-register.html')

@login_required(login_url='/loginuser')
def checkBalance(request):

   
    with grpc.insecure_channel('talk.ai.co.zw:50000') as channel:
           stub = users_pb2_grpc.userServiceStub(channel)
           user2=request.session['activeuser']
           information=users_pb2.request(username=user2, domain='localvoip.ai.co.zw')
           response=stub.GetBalance(information)

           print(response)
           ball=float(response.balance*0.00000000001674)
           bal = round(ball, 3)
           con={'succ':True,"response":response,'realbalance':bal}
    return render(request,'balance.html',con)
    # return HttpResponse(user2)

@login_required(login_url='/loginuser')
def rechargeAccount(request):

    # with grpc.insecure_channel('talk.ai.co.zw:50000') as channel:
    #     stub = payments_pb2_grpc.paymentsServiceStub(channel)
    #     information=payments_pb2.Payment(username='+263786103016', transaction='120 Minutes for $0.1', domain='localvoip.ai.co.zw')
    #     response = stub.MasweraseiPayNow(information)
    # return (HttpResponse(response.result))
    if request.method=='POST':
        if request.POST['pin']=="":
            messages.error(request,'The Pin Field Cannot be Null')
            return render(request,'rechargeAcc.html')
        else:
            with grpc.insecure_channel('talk.ai.co.zw:50000') as channel:
                stub = payments_pb2_grpc.paymentsServiceStub(channel)
                if request.POST['number']=="":
                    information=payments_pb2.requests(username=request.session['activeuser'],voucherPin=request.POST['pin'], domain='localvoip.ai.co.zw')
                else:
                     information=payments_pb2.requests(username=request.POST['number'],voucherPin=request.POST['pin'], domain='localvoip.ai.co.zw')

                response = stub.RedeemVoucher(information)
                    
                if response.status==1:
                    messages.error(request,'RechargeSuccessful')
                    return redirect('checkBalance')
                else:
                    messages.error(request,response.error.localizedDescription)
                    return render(request,'rechargeAcc.html')

    return render(request,'rechargeAcc.html')

    # return render(request,'forms-layouts.html')
def testVerification(number):

    with grpc.insecure_channel('talk.ai.co.zw:50000') as channel:
        stub = users_pb2_grpc.userServiceStub(channel)
        information=users_pb2.request(username=number, domain='localvoip.ai.co.zw')
        response=stub.SendVerificationCode(information)
        print(response)
        print(response.status)
        return (response)

def register(username,code,password):

    with grpc.insecure_channel('talk.ai.co.zw:50000') as channel:
        stub = users_pb2_grpc.userServiceStub(channel)
        information=users_pb2.request(username=username, domain='localvoip.ai.co.zw',verificationCode=code,password=password)
        response=stub.Register(information)
        return (response)        

def registerCooperate(request):
    request.session.flush()
    con = {
            "form": registerFormCooperate(),
            'captch':captcha()
        }   
            # number = random.randint(1000,9999)
            # form.save()
            # member =users.objects.get(number=request.POST['number'])
            # member.verificationCode=number
            # member.save()
            # print(number)
            # number={'numbers':request.POST['number']}
            # return render(request,'verify.html',number)
    return render(request,'cooperate.html',con)   


def checkCoperate(request):
    form=registerFormCooperate()
    form2=verifyForm()
    captch=captcha(request.POST)
    if request.method=="POST":
        form=registerFormCooperate(request.POST,request.FILES)
        captch=captcha(request.POST)
        if form.is_valid():
            if True:
                cooperate=cooperates()
                cooperate.companyname=request.POST['companyname']
                cooperate.email=request.POST['email']
                # cooperate.gsmnumber=request.POST['gsmnumber']
                cooperate.cr14=request.FILES["cr14"]
                cooperate.cr6=request.FILES["cr6"]
                cooperate.represantativeid=request.FILES["represantativeid"]
                cooperate.proofofresidence=request.FILES["proofofresidence"]
                cooperate.save()
                sendmail("Maswerasei Account Creation Request","\n\nHie..\n\n\nRequest for Maswerasei sent, Please check your email in the next 24 hours for feedback.,\n\nRegards,\nAfricom",[request.POST['email']])
                # notify elsa email here
                # resp=testVerification(form.cleaned_data.get('gsmnumber'))
                # number={'numbers':request.POST['gsmnumber'],'res':resp,"form2":form2}
            
                return render(request,'done.html')
            else:
                con = {
                    "form": registerFormCooperate(request.POST,request.FILES),
                    'captch':captcha(request.POST)
                    }
                return render(request,'cooperate.html',con)   
        else:
            con = {
                    "form": registerFormCooperate(request.POST,request.FILES),
                    'captch':captcha(request.POST)
                    }
            request.session['email']=request.POST['email'] 
            request.session['companyname']=request.POST['companyname']
    
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if cooperates.objects.filter(email=request.POST['companyname']).exists() :
                messages.success(request,"Company already Taken")
            messages.success(request,"Errors Found: Please make sure all fields are filled correctly")
            if users.objects.filter(email=request.POST['email']).exists() or cooperates.objects.filter(email=request.POST['email']).exists() :
                messages.success(request,"Email Taken")
            elif request.POST['email']=="":
                pass   
            elif re.fullmatch(regex, request.POST['email'])==None:
                messages.success(request,"Incorrect Email")
           
            if cooperates.objects.filter(companyname=request.POST['companyname']).exists():
                messages.success(request,"Company Name Taken")
           
            return redirect("checkCoperate")
            # return render(request,'cooperate.html',con)
    else:
        # con = {
        # "form": registerFormCooperate(None) ,
        # 'captcha':captcha()
        # }
        return render(request,'cooperate.html')

@login_required(login_url='/loginuser')
def profile(request):
    
    if users.objects.filter(gsmnumber=request.session['activeuser2']).exists():

        user=users.objects.get(gsmnumber=request.session['activeuser2'])
        cont={'user':user}
        return render(request,'users-profile.html',cont)  
    else:
        user=cooperates.objects.get(gsmnumber=request.session['activeuser2'])
        cont={'user':user}
        return render(request,'users-profile.html',cont)
   

@login_required(login_url='/loginuser')
def approveCoperate(request):
    con={"cooperates":cooperates.objects.all()}
    return render(request,'approve.html',con)

@login_required(login_url='/loginuser')
def downloadcr14(request,name):
     if 'admin' in request.session:
        if request.session['admin']:
            response = HttpResponse(content_type='file/pdf')
            image=cooperates.objects.get(companyname=name).cr14
            return FileResponse(image.open())  
     else:
        return HttpResponse(request,"<h1>Kwana</h1>")

 


@login_required(login_url='/loginuser')
def downloadcr6(request,name):

    response = HttpResponse(content_type='file/pdf')
    image=cooperates.objects.get(companyname=name).cr6 
    return FileResponse(image.open()) 
@login_required(login_url='/loginuser')
def downloadproofofresidence(request,name):

    response = HttpResponse(content_type='file/pdf')
    image=cooperates.objects.get(companyname=name).proofofresidence 
    return FileResponse(image.open()) 

@login_required(login_url='/loginuser')
def downloadrepresantativeid(request,name):

    response = HttpResponse(content_type='file/pdf')
    image=cooperates.objects.get(companyname=name).represantativeid
    return FileResponse(image.open()) 

 
@login_required(login_url='/loginuser')
def approved(request,name):
     if 'admin' in request.session:

         
            cooperate=cooperates.objects.get(companyname=name) 
            cooperate.approved=True
            cooperate.save()
            con={"cooperates":cooperates.objects.all()}
            messages.success(request,"The Company: "+cooperate.companyname+" has been approved!")
            sendmail("You have been approved to register for Maswerasei","Hi "+name+"\n\nYou have been approved to register for Maswerasei\n\nPlease use the link below to finish up registering\n\nhttp://127.0.0.1:8000/cooperatestep2/"+name+"\n\n\nRegards\nAfricom.",[cooperate.email])
            return render(request,'approve.html',con)
     else:
        return HttpResponse(request,"<h1>Kwana</h1>")
    
def cooperatestep2(request,name):
    con = {
            "form": registerFormCooperate(),
            'captch':captcha(),
            'companyname':name
        } 
    return render(request,"cooperatestep2.html",con) 


def registerCoperateCheck(request):

    form=cooperatestep2Form()
    form2=verifyForm()
    captch=captcha()
   
    if request.method=="POST":
        form=cooperatestep2Form(request.POST)
        captch=captcha(request.POST)
        if form.is_valid():
                if captch.is_valid():

                    companyname=request.POST['companyname']
                    cooperate=cooperates.objects.get(companyname=companyname)
                    email=cooperate.email
                    print(email)
                    cooperate.gsmnumber=form.cleaned_data.get('gsmnumber')
                    cooperate.password=form.cleaned_data.get('password')
                    cooperate.save()
                    if True:
                        realuser = User.objects.create_user(form.cleaned_data.get('gsmnumber'), email, form.cleaned_data.get('password'))
                        realuser.save()


                    resp=testVerification(form.cleaned_data.get('gsmnumber'))
                  
                    if resp.status==1:
                        number={'numbers':request.POST['gsmnumber'],'res':resp,"form2":form2,'password':request.POST['password'],'message':"Please enter the verification code we just sent to: "+request.POST['gsmnumber']}
                        return render(request,'verifybusiness.html',number)
                    elif resp==3:
                        number={'numbers':request.POST['gsmnumber'],'res':resp,"form2":form2,'password':request.POST['password'],"message":resp.error.localizedDescription}
                        return render(request,'verifybusiness.html',number)
                    
                    else:
                         messages.info(request,resp.error.localizedDescription)
                         con = {
                        "form": registerForm(request.POST),
                        'captch':captcha(),
                        'companyname':request.POST['companyname']
                    }
                         return render(request,'cooperatestep2.html',con)
                else:
                    con = {
                        "form": registerForm(request.POST),
                        'captch':captcha(request.POST),
                        'companyname':request.POST['companyname']
                    }
                    return render(request,'cooperatestep2.html',con)
        else:
            con = {
                "form": registerForm(request.POST),
                'captch':captcha(request.POST),
                'companyname':request.POST['companyname']
            }
            return render(request,'cooperatestep2.html',con)
    else:
        con = {
        "form": cooperatestep2Form(None) ,
        'captcha':captcha(),
        'companyname':request.POST['companyname']
            }
        return render(request,'cooperatestep2.html.html',con)


def verifybusiness(request):
    form2=verifyForm()
    if request.method=="POST":
        resp= register(request.POST['number'],request.POST['verificationcode'],request.POST['password'])       
        print(resp.status)
        print(resp)
        print(resp.error.localizedDescription)
        if resp.status==1:
            cooperate=cooperates.objects.get(gsmnumber=request.POST['number'])
            cooperate.registered=True
            cooperate.alliasNumber=resp.alias
            cooperate.save()
            request.session['activeuser']=request.POST['number']
            cont={'user':request.session['activeuser']}
            return render(request,'index.html',cont)

        else:
            messages.info(request,"Verification Failed, Please Try Again!")
            number={'numbers':request.POST['number'],'res':resp,"form2":form2,'password':request.POST['password']}
            return render(request,'verifybusiness.html',number)
        

def signout(request):
    request.session.flush()
    logout(request)
    messages.info(request,"You are Now Logged Out")
    return render(request,'pages-login.html')  

 
def customerMail(request):
    form=contactForm()
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            sendmail(request.POST['subject'],request.POST['message']+"\n\n\nCustomer Email: "+request.POST['email'],['munyaradzichirove@gmail.com'])
            messages.info(request,"Message Sent")
        else:
            
            context={'form':contactForm(request.POST)}
            return render(request,"contact.html",context)     
            
    return render(request,'contact.html')

def contact(request):            
    return render(request,'contact.html')

def faqs(request):            
    return render(request,'faqs.html')

def choose(request):
    return render(request,"choose.html")

@cache_page(60 * 15)
@csrf_protect
def loginuser(request):
    request.session.flush()
    form =loginForm()
    check=False
    checkuser=""
    if request.method=="POST":
        form=loginForm(request.POST)
        if form.is_valid():
            all=[]
            allusers=users.objects.all()
            allcooperates=cooperates.objects.all()
            all.append(allcooperates)
            all.append(allusers) 
        

            all = list(chain(allusers, allcooperates))
          
            for i in all:
                if i.gsmnumber==request.POST['number']:
                    check=True
                    checkuser=i
            if check==True:
                if checkuser.password==request.POST['password']: 
                    if checkuser.registered==True:
                        if checkuser.cdmanumber != None:
                            request.session['activeuser']=checkuser.cdmanumber
                            request.session['activeuser2']=checkuser.gsmnumber
                            request.session['cdma']=checkuser.cdmanumber
                            cont={'user':request.session['activeuser']} 
                        else:
                            request.session['activeuser']=checkuser.gsmnumber 
                            request.session['activeuser2']=checkuser.gsmnumber
                            cont={'user':request.session['activeuser']}     


 
 
                               

                        user = authenticate(request, username=checkuser.gsmnumber, password=request.POST['password'])
                        if user is not None:
                            login(request, user)
                            # return render(request,'index.html',cont) 
                            if checkuser.gsmnumber=="password" and checkuser.password=="password":
                                request.session['admin']="True"
                                return redirect('approveCoperate')
                            else:
                                return redirect('home')
                        
                        else:
                            messages.info(request,"username or password incorrect")
                            return render(request,'pages-login.html')   

                    else:
                        
                       
                        request.session['completed']=False
                        request.session['mobile']=request.POST['number']

                else:

                    messages.info(request,"username or password incorrect")
                    return render(request,'pages-login.html') 

            else:
                       
                    messages.info(request,"username or password incorrect")
                    return render(request,'pages-login.html')           
        else:
            messages.info(request,"Please make sure all fields are filled")
            return redirect('loginuser')         
    return render(request,'pages-login.html') 



def finishregistering(request):
    if request.method=="POST":
        try:
            form2=verifyForm(request.POST)
            users.objects.get(gsmnumber=request.session['mobile'])
            user= users.objects.get(gsmnumber=request.session['mobile']) 
            user.gsmnumber=request.POST['mobile']
            user.save()
            resp=testVerification(form2.cleaned_data.get('gsmnumber'))
            if resp.status==1:
                number={'numbers':request.POST['mobile'],'res':resp,"form2":form2,'password':'','message':"Please enter the verification code we just sent to: "+request.POST['mobile']}
                return render(request,'verify.html',number)
            elif resp==3:
                messages.info(request,resp.error.localizedDescription)
                con = {
                "form": registerForm(request.POST),
                'captch':captcha()
            }
                number={'numbers':request.POST['mobile'],'res':resp,"form2":form2,'password':'',"message":resp.error.localizedDescription}
                return render(request,'pages-register.html',con)
            
            else:
                    messages.info(request,resp.error.localizedDescription)
                    con = {
                "form": registerForm(request.POST),
                'captch':captcha()
            }
                    return render(request,'pages-register.html',con)

        except:
            user=cooperates.objects.get(gsmnumber=request.session['mobile'])  
            user.gsmnumber=request.POST['mobile'] 
            user.save() 
            resp=testVerification(form2.cleaned_data.get('gsmnumber'))
               
            
            if resp.status==1:
                number={'numbers':request.POST['mobile'],'res':resp,"form2":form2,'password':'','message':"Please enter the verification code we just sent to: "+request.POST['mobile']}
                return render(request,'verify.html',number)
            elif resp==3:
                messages.info(request,resp.error.localizedDescription)
                con = {
                "form": registerForm(request.POST),
                'captch':captcha()
            }
                number={'numbers':request.POST['mobile'],'res':resp,"form2":form2,'password':'',"message":resp.error.localizedDescription}
                return render(request,'pages-register.html',con)
            
            else:
                    messages.info(request,resp.error.localizedDescription)
                    con = {
                "form": registerForm(request.POST),
                'captch':captcha()
            }
                    return render(request,'pages-register.html',con)

    else:

        return HttpResponse('not done')   


def paynow(request):

    paynow = Paynow(
    '15942', 
    'a3d6c330-7589-4542-bfa8-51385a5b3f7d',
    'http://google.com', 
    'http://google.com'
    )

    payment = paynow.create_payment('Order', 'munyaradzichirove@gmail.com')

    payment.add('Payment for stuff', 1)

    response = paynow.send_mobile(payment, '0786103016', 'ecocash')


    if(response.success):
        poll_url = response.poll_url

        print("Poll Url: ", poll_url)

        status = paynow.check_transaction_status(poll_url)

        time.sleep(30)

        print("Payment Status: ", status.status)
        reset_paynow_connection()
        
        return HttpResponse("done")


    else:
        return HttpResponse("error")
    


def reset_paynow_connection():
    url = 'https://www.paynow.co.zw/interface/initiatetransaction'
    params = {
        'id': '15942',
        'reference': 'Order',
        'amount': 1,  # Replace with your transaction amount
        'additionalinfo': 'Additional transaction information',
        'returnurl': 'https://www.google.com/return',
        'resulturl': 'https://www.google.com/result'
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        session_id = response.text.strip()
        return session_id
    else:
        raise Exception('Failed to reset Paynow connection')    
    


    

# error 2 response.status
def  voucher(request):


    with grpc.insecure_channel('talk.ai.co.zw:50000') as channel:
        stub = payments_pb2_grpc.paymentsServiceStub(channel)
        information=payments_pb2.requests(username='+263786103016',voucherPin='23032171328613', domain='localvoip.ai.co.zw')
        response = stub.RedeemVoucher(information)
        if response.status==2:
            print(response.status)
            print(response.error.localizedDescription)

        else:
            print('done')    
    return (HttpResponse(response.status))       
    
    

        













                        
              
                      


  





    
 
 





 