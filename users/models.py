from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ContactInfo(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    email = models.CharField(max_length=200,blank=True)
    phonenumber = models.CharField(max_length=20,blank=True)
    instagram_url = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.user.username
