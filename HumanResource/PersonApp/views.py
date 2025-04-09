from django.shortcuts import render
from .models import Perosn



def index(request):
    context = {'segment': 'index'}
    context['person'] = Perosn.objects.all()
    return render(request, "index.html", context=context)


def personPage(request,id):
    context = {'segment': 'index'}
    #context['p'] = Perosn.objects.filter(id=id).last()
    context['p'] = Perosn.objects.get(id=id)
    
    print(Perosn.objects.filter(id=id))
    return render(request, "person.html", context=context)
