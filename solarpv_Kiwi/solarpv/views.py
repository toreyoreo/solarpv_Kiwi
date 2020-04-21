from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'solarpv/homepage.html')

def login(request):
    return render(request, 'solarpv/login.html')

def registration(request):
    return render(request, 'solarpv/registration.html')