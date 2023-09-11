from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('home',home,name='home'),
    path('about/',views.about,name='about'),
    path('rooms/',rooms,name='rooms'),
   
    path('service/',service,name='service'),
    path('gym/',gym,name='gym'),
    path('booking/<str:pk>/', booking, name="booking"),

    
]
