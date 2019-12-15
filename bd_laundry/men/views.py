from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def men(request):
    return render(request,'men.html')
