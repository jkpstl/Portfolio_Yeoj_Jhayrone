from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def jhayrone_profile(request):
    return render(request, 'jhayrone.html') 

def yeoj_profile(request):
    return render(request, 'yeoj.html') 

def projects(request):
    return render(request, 'projects.html') 