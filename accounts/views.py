from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kwargs):
    return render(request, 'signin.html')

def signup(request, *args, **kwargs):
    if request.method == 'POST':
        pass
    return render(request, 'signup.html')