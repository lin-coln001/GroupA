from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='students/',null=True,blank=True)
    name =models.CharField(max_length=20)
    course =models.CharField(max_length=20)
    age =models.IntegerField()
    email =models.EmailField(null=True, blank=True )
    date =models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField()
    checkout_request_id = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone