from django.shortcuts import render
from django.http import HttpResponse
from .models import my_order

# Create your views here.
def order(request):
    return render(request,"order.html")

def order_list(request):
    #print(request.POST.__dict__)

    name=request.POST.get("name")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    flat=request.POST.get("flat")
    house=request.POST.get("house")
    avenue=request.POST.get("avenue")
    road=request.POST.get("road")
    my_order_obj=my_order(name=name, email=email,phone=phone,flat=flat,house=house,avenue=avenue,road=road)
    my_order_obj.save()
    return render(request,"order.html")
