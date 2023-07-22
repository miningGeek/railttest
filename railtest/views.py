from django.shortcuts import render, redirect

# Create your views here.

#some crap
def home(request):

    context = {}

    return render(request,'railtest/home.html', context)