from django.shortcuts import render
from myapp.models import *
from myapp.forms import Application
# Create your views here.

def home(request):
    courses = Course.objects.all()
    teachers=Teacher.objects.all()
    return render(request, 'home.html', {'courses': courses , 'teachers': teachers})

# about_detail funksiyasi
def about_detail(request, pk):
    course = Course.objects.get(pk=pk)      
    form = Application(request.POST or None)
    is_success=False
    if request.method == 'POST' and form.is_valid():
        is_success=True
        form.save()
        form = Application()
    return render(request, 'about_detail.html', {'course': course,'form':form,'is_success':is_success})
