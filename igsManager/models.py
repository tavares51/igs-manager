from django.db import models


# Create your models here.
class Departament(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length = 256)
    email = models.EmailField(max_length = 254)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
