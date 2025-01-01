from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def lost(request):
    return redirect('home')

def account(request):
    return render(request, 'home.html')

def analytics(request):
    return render(request, 'home.html')

def templates(request):
    return render(request, 'home.html')

