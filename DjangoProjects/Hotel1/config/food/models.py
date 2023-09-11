from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Food(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    category=models.ForeignKey(Category, default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name 

    def snippet(self):
        return self.description[:80] + '...more' 






class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.food.name
    
    def total_price(self):
        return self.food.price * self.quantity




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.IntegerField(blank = True)
    total_price = models.IntegerField()
    def __str__(self):
        return 'Order # %s' % (str(self.id))




class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_food')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    total_price = models.IntegerField()
    def __str__(self):
        return '%s %sx - %s' % (self.food, self.total_quantity, self.order.user.username)

