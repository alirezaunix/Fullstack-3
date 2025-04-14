from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=250,verbose_name="Full Name")
    phone1=models.CharField(max_length=15 , verbose_name="Phone 1")
    phone2=models.CharField(max_length=15,null= True,blank=True,verbose_name="Phone 2")
    clientType=models.BooleanField(default=False,verbose_name="Owner=True, Seeker=False")
    
class House(models.Model):
        id = models.AutoField(primary_key=True)
        regdate=jmodels.jDateField()
        location=models.CharField(max_length=100)
        address=models.TextField()
        rooms=models.IntegerField(default=1)
        size=models.IntegerField(default=1)
        buildingyear=models.IntegerField(default=1)
        owner=models.ForeignKey("Client",on_delete=models.CASCADE)
        