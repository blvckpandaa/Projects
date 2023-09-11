from datetime import date
import datetime
from django.db import models

class Rooms(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=100)
    bed=models.CharField(max_length=100)
    services=models.TextField()
    
    def __str__(self):
        return self.name
    

    
class Reservation(models.Model):
    guest_name = models.CharField(max_length=100)   
    email = models.EmailField(blank=True)
    request = models.TextField(null=True)
    room = models.ForeignKey(Rooms,on_delete=models.CASCADE)



    
    





    
    
    
    

    
    
    