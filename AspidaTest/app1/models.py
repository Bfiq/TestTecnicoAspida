from django.db import models
from django.contrib.auth.models import User

class Brands(models.Model):
    name = models.CharField(max_length=80)  #tipo de datos de modelos en este caso "Varchar"

    def __str__(self):
        return self.name

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username