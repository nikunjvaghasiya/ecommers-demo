from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm
from django.http.response import HttpResponseRedirect

def index(request, *args, **kwargs):
    return render(request, 'signin.html')

def signup(request, *args, **kwargs):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'signup.html')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('name')
            
            return HttpResponseRedirect('/dashboard')
    else:
        form = SignupForm()    
    
    return render(request, 'signup.html', {"form": form})


def dashboard(request):
    return render(request, 'dashboard.html')