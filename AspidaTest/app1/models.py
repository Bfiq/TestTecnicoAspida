from django.db import models

class Brands(models.Model):
    name = models.CharField(max_length=80)  #tipo de datos de modelos en este caso "Varchar"

    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    document = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name