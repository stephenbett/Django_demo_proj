from curses.ascii import HT
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from  .models import Trip

 # Returning views without Templates
        # def index(request):
        # return HttpResponse("Europe Trips")

# With Templates
def index(request):
    
    context = {
        'trips': Trip.objects.all()
    }
    return render(request,"index.html", context)
 