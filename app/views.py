from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def account(request):
    return render(request, 'account.html')

def analytics(request):
    return render(request, 'analytics.html')

def templates(request):
    return render(request, 'templates.html')

def lost(request):
    return redirect('home')

