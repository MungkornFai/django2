from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
a = '<center style="background:blue;"><h1>This is home page</h1></center>'

def Home(request):
    return render(request, 'home/index.html')

