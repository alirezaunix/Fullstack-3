from django.shortcuts import render
from .models import Client


def regclient(request):
    if request.method=="POST":
        formdict=dict(request.POST)
        fullname = formdict.get('fullname')[0]
        phone1 = formdict.get('phone1')[0]
        phone2 = formdict.get('phone2')[0]
        owner = formdict.get('userType')[0]
        if owner=="seeker":
            flag=False
        else:
            flag=True
        #print(owner)
        
        Client.objects.create(fullname=fullname, phone1=phone1,
                                  phone2=phone2, clientType=flag).save()
    
        
        #print(fullname, phone1, phone2, owner)
    return render(request, "regclient.html")

def reghouse(request):
    return render(request,"reghouse.html")

