from http.client import HTTPResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Users, Brands
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "app1/index.html")

def register(request):
    list_brands = Brands.objects.all()
    return render(request, "app1/register.html",{
        "list_brands": list_brands
    })

def users(request):
    list_users = Users.objects.all()
    return render(request, "app1/users.html", {
        "list_users": list_users
    })

def registerFormUser(request):
    if request.method == 'POST':
        try:
            name = request.POST["names"]
            lastname = request.POST["lastname"]
            id = request.POST["id"]
            password = request.POST["password"]
            select = request.POST["select"]
            
        except(KeyError, Users.DoesNotExist):
            return render(request, "app1/register.html",{
                "error_message": "No has llenado todos los campos"
            })
        else:
            brand= get_object_or_404(Brands, pk=select)
            user = Users(name=name,lastName=lastname,document=id,password=password,brand_id=brand)
            user.save()
            print(user)
            return HttpResponseRedirect(reverse("app1:index"))
    else:
        return render(request, "app1/register.html",{
                "error_message_http": "Ha ocurrido un error"
            })

def login():
    return HTTPResponse("hola")