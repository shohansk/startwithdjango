from django.shortcuts import render
from django.http import HttpResponse
from .models import aboutus


def employee(request):
    return HttpResponse("This  is employee page")
def profile(request):
    aboutdata=aboutus.objects.all()[0]
    context ={
        'about':aboutdata
    }
    return render(request ,'employee/profile.html',context)

