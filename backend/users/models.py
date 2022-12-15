from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=32,default=None,null=True)
    username=models.CharField(max_length=256,default=None,null=True)
    email=models.EmailField(max_length=256,default=None,null=True)
    website=models.CharField(max_length=256,default=None,null=True)
