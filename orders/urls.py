from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("winkelwagen", views.winkelwagen, name="winkelwagen"),
    path("home", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("commit_order", views.commit_order, name="commit_order"),
    path("toppings", views.toppings, name="toppings"),
    path("commit_all_order", views.commit_all_order, name="commit_all_order"),
    path("show_orderlist", views.show_orderlist, name="show_orderlist"),
]
