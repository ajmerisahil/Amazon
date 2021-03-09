from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})

def blogpost(request, id ):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request , 'blog/blogpost.html' , {'post':post} )








def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")


#def index(request):
#    return HttpResponse('Blog Home')

