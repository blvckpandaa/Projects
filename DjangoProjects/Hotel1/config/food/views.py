from unicodedata import category
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *




def food_list(request):
    foods=Food.objects.all()

    categories=Category.objects.all()
    category=request.GET.get('category')
    foods=Food.objects.all()
    search=request.GET.get('search')
    f = request.GET.get('f')
    foods=foods.filter(Q(name__icontains=search)) if search else foods
    foods=foods.filter(category=category) if category else foods

    food_id = request.GET.get('food')

    if food_id:
        food = Food.objects.get(pk = food_id)
        cart_item = CartItem.objects.filter(food = food)
        if not cart_item:
            cart_item = CartItem.objects.create( customer=request.user, food=food, quantity=1 )
            cart_item.save()
            return redirect('food')
        for item in cart_item:
            item.quantity += 1
            item.save()
            return redirect('food')


    return render(request, 'food.html', {'foods':foods, 'categories':categories})



def cart(request):
    cart_item = CartItem.objects.filter(customer = request.user)
    quantity = sum([item.quantity for item in cart_item])
    total_price = sum([item.total_price() for item in cart_item])
    if not cart_item:
        return redirect('food')

    return render(request, 'cart.html', {'cart_item':cart_item, 'quantity':quantity, 'total_price':total_price})




def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk = pk).delete()
    return redirect('cart')




def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk = pk)
    action  = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')
    




def order(request):
    error = False
    cart_item = CartItem.objects.filter(customer = request.user)
    total_price = sum([item.total_price() for item in cart_item])
    total_quantity = sum([item.quantity for item in cart_item])
    error = False
    form = OrderForm(request.POST)

    if request.method=='POST':
        if form.is_valid():
            order = Order.objects.create(
                user = request.user,
                address = request.POST.get('address'),
                phone = request.POST.get('phone'),
                total_price = total_price,
            )
            for item in cart_item:
                OrderProduct.objects.create(
                    order = order,
                    food = item.food,
                    total_quantity = item.quantity,
                    total_price = item.total_price(),
                )
            cart_item.delete()
            return redirect('food')
        if not form.is_valid():
            error = True

    form = OrderForm()
    return render(request, 'order_creation_page.html', {'cart_item':cart_item, 'total_price':total_price, 'total_quantity':total_quantity, 'form':form, 'error':error})



def orders(request):
    orders = Order.objects.filter(user = request.user)
    if not orders:
        return redirect('food')
    return render(request, 'orders.html', {'orders':orders})



def delete_order(request, pk):
    order = Order.objects.get(pk = pk).delete()
    return redirect('orders')
    


