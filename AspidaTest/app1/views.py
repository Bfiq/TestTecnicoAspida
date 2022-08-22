from contextlib import redirect_stderr
from django.shortcuts import render, get_object_or_404, redirect
from .models import Users, Brands
from django.contrib.auth.models import User
from .forms import formRegister

def index(request):
    return render(request, "app1/index.html")

def register(request):
    list_brands = Brands.objects.all()
    if request.method == 'POST':
        form = formRegister(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST["username"]
            select = request.POST["select"]
            brand= get_object_or_404(Brands, pk=select)
            user= get_object_or_404(User, username=username)
            app1_user = Users(user=user,brand_id=brand)
            app1_user.save()
            return redirect('app1:login')
            #return render(request, "app1/login.html")
    else:
        form = formRegister()

    context = {'form' : form,
               "list_brands": list_brands}
    return render(request, 'app1/register.html', context)

def users(request):
    list_users = Users.objects.all()
    return render(request, "app1/users.html", {
        "list_users": list_users
    })

def modelbd(request):
    return render(request, "app1/modelbd.html")