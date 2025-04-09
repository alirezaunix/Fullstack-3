from django.shortcuts import render
from .models import Perosn



def index(request):
    context = {'segment': 'index'}
    context['person'] = Perosn.objects.all()
    return render(request, "index.html", context=context)


