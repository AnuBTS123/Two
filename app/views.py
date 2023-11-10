from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Anu(request):
    return HttpResponse('<h1><marquee>From Anu To Abi: How are You Abi</h1></marquee>')

def Abi(request):
    return HttpResponse('<h1><marquee>Reply:I am fine Anu how are you</h1></marquee>')
