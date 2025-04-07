from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post


def index(request):
    context = {'segment': 'index'}
    context['data'] = Post.objects.all()
    return render(request, "index.html",context=context)





def hi(request):
    print(request.user)
    print(request.method)
    return HttpResponse("Hi!!!!!")

def bye(request):
    return HttpResponse("Bye!!!!!!!")


def product(request, num):
    return HttpResponse(f"YourProdct is {num}")

