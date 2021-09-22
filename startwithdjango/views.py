
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    text ={
        "name": "Abdul Alim Shohan",
        "age" : 29,
        "number": "01516132985",
        'friends_name':['shohag','saiab','sakib','mizan','siam','samir']
    }
    return render(request,'index.html',text)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
