from django.contrib import admin
from .models import Users
from .models import Brands

admin.site.register(Users)#registro de los modelos
admin.site.register(Brands)