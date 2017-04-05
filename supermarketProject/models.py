from django.db import models

# Create your models here.

class Person(models.Model):

    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.IntegerField() # 1 manager , 2 emplyee , 3 customer
    gmail = models.CharField(max_length=50)


    def __str__(self):
        return self.name



class Supermarket(models.Model):

    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=50)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


