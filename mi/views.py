from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohith(request):
    return HttpResponse("<h1>rohith is winning captain</h1>")
