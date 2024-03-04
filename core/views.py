from django.shortcuts import render
from django.core.signals import request_finished
from django.dispatch import receiver

# Create your views here.

def home(request):
    name = 'prime'

    return render(request,'home.html',{
        'name': name,
    }) 

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print('Request finished!')

def detail(request):
    cat = ['prime','debbie']

    return render(request, 'detail.html',{
        'categories':cat,
    })