from django.db import models

class users(models.Model):
    email=models.CharField(max_length=100)
    gsmnumber=models.CharField(max_length=100)
    cdmanumber=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=50)
    registered=models.BooleanField(default=False,null=True,blank=True)
    requestVerificationCode=models.IntegerField(default=1)
    allocatedNumber=models.IntegerField(default=0)
    alliasnumber=models.CharField(default='null',max_length=12)

    def __str__(self):
        return self.email




class cooperates(models.Model):
    companyname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gsmnumber=models.CharField(null=True,blank=True,max_length=100)
    password=models.CharField(null=True,blank=True,max_length=50)
    cdmanumber=models.CharField(null=True,blank=True,max_length=100)
    registered=models.BooleanField(null=True,blank=True,default=False)
    cr6=models.FileField(default='null',upload_to='pdfs')
    cr14=models.FileField(default='null',upload_to='pdfs')
    represantativeid=models.FileField(default='null',upload_to='pdfs')
    proofofresidence=models.FileField(default='null',upload_to='pdfs')
    approved=models.BooleanField(default=False,null=True,blank=True)
    alliasnumber=models.CharField(default=0,max_length=12)

    def __str__(self):
        return self.companyname       


class code(models.Model):
  code=models.CharField(max_length=4)
  def __str__(self):
        return self.code        
