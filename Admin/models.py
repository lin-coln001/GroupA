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