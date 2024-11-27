from django.shortcuts import render 
from django.http import HttpResponse 

# Create your views here.  

def captain(request):
    return HtppResponse('rohit is a captain of mumbai indians')
