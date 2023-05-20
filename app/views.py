from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def srujana(request):
    return HttpResponse("<marquee><h1>srujana Tinnavara</h1></marquee> ")

def revi(request):
    return HttpResponse("<marquee><i>Sollinga MammaKutti</i></marquee>")