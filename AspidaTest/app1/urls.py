from django.urls import path

from . import views

app_name = "app1"
urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("register", views.register, name="register"),
    path("a", views.login, name="login"),
    path("b", views.registerFormUser, name="registerFormUser")
]