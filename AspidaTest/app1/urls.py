from re import template
from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "app1"
urlpatterns = [
    path("users", views.users, name="users"),
    path("register", views.register, name="register"),
    path("", LoginView.as_view(template_name='app1/login.html'), name="login"),
    path("logout", LogoutView.as_view(template_name='app1/index.html'), name="logout"),
    path("modelbd", views.modelbd, name="modelbd"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)