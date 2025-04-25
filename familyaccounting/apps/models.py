from django.db import models

class Family(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=250)
    tel=models.CharField(max_length=20)
    


class IOMoney(models.Model):
    id=models.AutoField(primary_key=True)
    familymember=models.ForeignKey(Family,on_delete=models.CASCADE)
    money=models.FloatField(default=0)
    desc=models.CharField(max_length=500)
    iodate=models.DateField()
    addeddate=models.DateField(auto_created=True)
    