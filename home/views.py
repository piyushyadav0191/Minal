from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
       return render(request,'signup.html')

def login(request):
       return render(request,'login.html')

def calendar(request):
       return render(request,'calendar.html')

def contact(request):
       return render(request,'contact.html')