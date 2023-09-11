from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def rooms(request):
    rooms=Rooms.objects.all()

    return render(request, 'room.html', {'rooms':rooms,})



def roomdetails(request,pk):
    return render(request,'roomdetails.html')

def service(request):
    return render(request,'service.html')
def gym(request):
    return render(request,'gym.html')




def booking(request,pk):
    room = Rooms.objects.get(pk=pk)
    if request.method == "POST":
        error = ''
        form = ReservationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.room = room
            instance.save()
            return redirect('home')
        else:
            error = "Page not found"
    form = ReservationForm()
    return render(request,'booking.html',{'form':form,'room':room})
    

    

