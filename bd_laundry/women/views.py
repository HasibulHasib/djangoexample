from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def women(request):
    return render (request,'women.html')
