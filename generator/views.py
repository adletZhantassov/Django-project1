from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def index(request):
    return render(request, 'generator/home.html', {'password': 'qweasc123'})

def password(request):

    characters = list('abcdefghijklmnoprstuwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPRSTUWVXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')
    if request.GET.get('numbers'):
        characters.extend('123456789')
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})