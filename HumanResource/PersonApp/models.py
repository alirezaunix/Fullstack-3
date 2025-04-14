from django.db import models

class Perosn(models.Model):
    id=models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50,verbose_name=" First Name")
    lname = models.CharField(max_length=255, verbose_name=" Last Name")
    age = models.IntegerField(default=0, verbose_name="Age")
    gender =models.BooleanField(
        default=True, verbose_name="Gender , True=MAN")  # man True//woman False
    phone = models.CharField(max_length=15, verbose_name=" Phone Number",null=True,blank=True)
    birthdate=models.DateField(null=True,blank=True)
    photo = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.fname} {self.lname}"


    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
