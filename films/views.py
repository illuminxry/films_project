from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse   # added 
def home(request): 
    return render(request, 'home.html')
def main(request): 
    return render(request, 'films/main.html')
def user_info(request): 
    return render(request, 'films/user_info.html')