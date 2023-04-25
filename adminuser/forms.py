from django.forms import ModelForm
from django import forms
from selfServiceApp.models import users
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from selfServiceApp.models import users,cooperates
from itertools import chain


class registerForm(forms.Form):
   
    email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter email','required':True}))
    gsmnumber=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'leave blank if you dont have','required':True}))
    cdmanumber=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password again','required':True}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password','required':True,'min':3}))
    confirmpassword=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password again','required':True}))


    def clean_confirmpassword(self):
        data=self.cleaned_data.get('confirmpassword')
        data2=self.cleaned_data.get('password')
        if data!=data2:
            raise forms.ValidationError("passwords did not match")
        elif (len(data))<3:
            raise forms.ValidationError("minimum is 8 charaters")   
        elif  (len(data))>15:
            raise forms.ValidationError("minimum is 8 charaters")     

        return data   


    def clean_gsmnumber(self):
        data=self.cleaned_data.get('gsmnumber')
        user=users.objects.all()
        cooperate=cooperates.objects.all()

        model_combination = list(chain(user,cooperate))
        
        value=False
        for i in model_combination:
            if i.gsmnumber==data:
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("number already taken")  


    def clean_cdmanumber(self):
        data=self.cleaned_data.get('cdmanumber')
        user=users.objects.all()
        cooperate=cooperates.objects.all()

        model_combination = list(chain(user,cooperate))
        
        value=False
        for i in model_combination:
            if i.cdmanumber==data and i.cdmanumber!="" :
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("cdma number already taken")  


    def clean_email(self):
        data=self.cleaned_data.get('email')
        user=users.objects.all()
        value=False
        for i in user:
            if i.email==data:
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("email already taken")  
                     
class captcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    def clean_captcha(self):
        data=self.cleaned_data.get('captcha')
        
        if data=="":
            raise forms.ValidationError("kwana")  

        return data    
    
class registerFormCooperate(forms.Form):
   
    companyname= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter company number','required':True}))
    email= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter email','required':True}))
    cr6=forms.FileField(widget=forms.FileInput(attrs={'class': 'forms-control','placeholder': 'enter password','required':True}))
    cr14=forms.FileField(widget=forms.FileInput(attrs={'class': 'forms-control','placeholder': 'enter password','required':True}))
    represantativeid=forms.FileField(widget=forms.FileInput(attrs={'class': 'forms-control','placeholder': 'enter password','required':True}))
    proofofresidence=forms.FileField(widget=forms.FileInput(attrs={'class': 'forms-control','placeholder': 'enter password','required':True}))
 




    # gsmnumber= forms.CharField(required=False, empty_value=None,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter number','required':True}))
    # password=forms.CharField(required=False, empty_value=None,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password','required':True,'min':4}))
    # confirmpassword=forms.CharField(required=False, empty_value=None,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password again','required':True}))
    




    # def clean_confirmpassword(self):
    #     data=self.cleaned_data.get('confirmpassword')
    #     data2=self.cleaned_data.get('password')
    #     if data!=data2:
    #         raise forms.ValidationError("passwords did not match")
    #     elif (len(data))<3:
    #         raise forms.ValidationError("minimum is 8 charaters")   
    #     elif  (len(data))>15:
    #         raise forms.ValidationError("minimum is 8 charaters")     

    #     return data    
    # def clean_gsmnumber(self):
    #     data=self.cleaned_data.get('gsmnumber')
    #     user=users.objects.all()
    #     value=False
    #     for i in user:
    #         if i.gsmNumber==data:
          
    #             value=True

    #     if value==False:
    #         return data        
    #     else:  
    #         raise forms.ValidationError("number already taken")  


    def clean_gsmnumber(self):
        data=self.cleaned_data.get('gsmnumber')
        user=users.objects.all()
        cooperate=cooperates.objects.all()


        model_combination = list(chain(user,cooperate))
        
        value=False
        for i in model_combination:
            if i.gsmnumber==data:
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("number already taken")

    def clean_email(self):
        data=self.cleaned_data.get('email')
        user=users.objects.all()
        value=False
        for i in user:
            if i.email==data:
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("email already taken")  

    def clean_companyname(self):
        data=self.cleaned_data.get('companyname')
        cooperate=cooperates.objects.all()
        value=False
        for i in cooperate:
            if i.companyname==data:
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("companyname already taken")         
                     
class verifyForm(forms.Form):
    verificationcode= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter code here',}))
              
class loginForm(forms.Form):
   
    number=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'leave blank if you dont have','required':True}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password','required':True,'min':3}))
    
class cooperatestep2Form(forms.Form):
    gsmnumber=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'leave blank if you dont have','required':True}))
    cdmanumber=forms.CharField(required=False, empty_value=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password again','required':False,'empty_value':None}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password','required':True,'min':3}))
    confirmpassword=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter password again','required':True}))


    def clean_confirmpassword(self):
        data=self.cleaned_data.get('confirmpassword')
        data2=self.cleaned_data.get('password')
        if data!=data2:
            raise forms.ValidationError("passwords did not match")
        elif (len(data))<3:
            raise forms.ValidationError("minimum is 8 charaters")   
        elif  (len(data))>15:
            raise forms.ValidationError("minimum is 8 charaters")     

        return data   


    def clean_gsmnumber(self):
        data=self.cleaned_data.get('gsmnumber')
        user=cooperates.objects.all()
        value=False
        for i in user:
            if i.gsmnumber==data:
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("number already taken")  

    def clean_email(self):
        data=self.cleaned_data.get('email')
        user=users.objects.all()
        value=False
        for i in user:
            if i.email==data:
          
                value=True

        if value==False:
            return data        
        else:  
            raise forms.ValidationError("email already taken")  
        


class contactForm(forms.Form):
   
    email=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'leave blank if you dont have','required':True}))
    message=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'leave blank if you dont have','required':True}))
    subject= email=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'leave blank if you dont have','required':True}))
   


    def clean_confirmpassword(self):
        data=self.cleaned_data.get('confirmpassword')
        data2=self.cleaned_data.get('password')
        if data!=data2:
            raise forms.ValidationError("passwords did not match")
        elif (len(data))<3:
            raise forms.ValidationError("minimum is 8 charaters")   
        elif  (len(data))>15:
            raise forms.ValidationError("minimum is 8 charaters")     

        return data   
