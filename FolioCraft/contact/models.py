from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)