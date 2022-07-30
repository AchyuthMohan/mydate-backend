from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    message=models.TextField(max_length=200)
    email=models.EmailField(max_length=100)
    auth_phno=models.IntegerField(blank=True)
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name