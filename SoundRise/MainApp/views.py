from django.shortcuts import render

def index(request):
    return render(request, 'MainApp/index.html')

def explore(request):
    return render(request, 'MainApp/explore.html')

def login(request):
    return render(request, 'MainApp/login.html')