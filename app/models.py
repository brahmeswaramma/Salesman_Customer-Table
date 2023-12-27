from django.db import models

# Create your models here.
class Salesman(models.Model):
    salesman_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    commission=models.IntegerField()
    def __str__(self):
       return str(self.salesman_no)
    

class Customer(models.Model):
        customer_no=models.IntegerField(primary_key=True)
        cus_name=models.CharField(max_length=100)
        city=models.CharField(max_length=100)
        grade=models.IntegerField()
        salesman_no=models.ForeignKey(Salesman,on_delete=models.CASCADE)
        email=models.EmailField(default='india@gmail.com')

        def __str__(self):
           return self.cus_name