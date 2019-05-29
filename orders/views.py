from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Products, Orders, All_orders
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        'products':Products.objects.all()
    }
    return render(request,"index.html", context)

def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirmation"]
        user = authenticate(username=username)
        if username == "" or email is "" or password is "":
            return render(request,"register.html", {'message':"Fill in all fields"})
        if password is not confirm:
            return render(request,"register.html", {'message':"Passwords are not the same"})
        if user is None:
            return render(request,"register.html", {'message':"Username is already in use"})

        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"register.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def toppings(request):
    product_id = request.POST["product_id"]
    context = {
        'all_toppings':Products.objects.filter(categorie__exact='toppings'),
        'product':Products.objects.get(pk=product_id)
    }
    return render(request, "toppings.html",context)

def winkelwagen(request):
    orders = Orders.objects.filter(username__exact=request.user)
    total_price = 0
    for order in orders:
        total_price +=order.price

    context = {
        'total_price':round(total_price,2),
        'orders':orders,
        'amount':len(orders)
    }
    return render(request,"winkelwagen.html",context)

def commit_order(request):
    size = request.POST["button"]
    current_user = request.user
    product_id = request.POST["product"]
    product = Products.objects.get(pk=product_id)

    if size == "Cancel":
        return HttpResponseRedirect(reverse("index"))
    elif size == 'small':
        price = product.price_small
    elif size == 'large':
        price = product.price_large

    try:
        topping1 = request.POST["topping1"]
    except:
        topping1 = None

    try:
        topping2 = request.POST["topping2"]
    except:
        topping2 = None

    try:
        topping3 = request.POST["topping3"]
    except:
        topping3 = None

    try:
        extra_cheese = request.POST["cheese"]
        price += 0.5
    except:
        extra_cheese = False
    order = Orders.objects.create(username=current_user,
                                    product=product.product,
                                    topping1=topping1,
                                    topping2=topping2,
                                    topping3=topping3,
                                    extra_kaas=extra_cheese,
                                    price=price)
    return HttpResponseRedirect(reverse("index"))

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def show_orderlist(request):
    orders = All_orders.objects.all()
    users = []
    for order in orders:
        if not order.username in users:
            users.append(order.username)
    if request.method == "GET":
        total_price = 0
        context = {
            'total_price':round(total_price,2),
            'users':users
        }
        return render(request, "superuser_orderlist.html", context)
    else:
        try:
            total_price = 0
            for order in orders:
                total_price +=order.price
            context = {
                'total_price':round(total_price,2),
                'users':users,
                'orders':All_orders.objects.filter(username__exact=request.POST['user'])
            }
            return render(request, "superuser_orderlist.html", context)
        except:
            total_price = 0
            All_orders.objects.filter(username__exact=request.POST['done']).delete()
            orders = All_orders.objects.all()
            users = []
            for order in orders:
                if not order.username in users:
                    users.append(order.username)
            context = {
                'total_price':round(total_price,2),
                'users':users
            }
            return render(request, "superuser_orderlist.html", context)

def commit_all_order(request):
    orders = Orders.objects.filter(username__exact=request.user)
    for order in orders:
        order = All_orders.objects.create(username=request.user,
                                        product=order,
                                        price=order.price)
    Orders.objects.filter(username__exact=request.user).delete()
    return HttpResponseRedirect(reverse("index"))
