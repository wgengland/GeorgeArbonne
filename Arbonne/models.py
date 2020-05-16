from django.db import models
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
import requests
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_url =  models.CharField(max_length = 500)
    product_name = models.CharField(max_length=200,default = "Will be filled automatically")
    pub_date = models.DateTimeField(default = timezone.now)
    product_description = models.TextField(max_length=1000,editable=False)
    product_price = models.FloatField(editable=False)
    image_url = models.CharField(max_length=300,editable=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('accountprofile')

    def save(self, *args, **kwargs):
        response = requests.get(self.product_url)
        data = response.text
        listing_soup = BeautifulSoup(data,features='html.parser')
        product_info = listing_soup.find("div",class_="product_info")#soup.find_all("div",class_="product_grid")#.find_all("div",class_="grid_item")
        self.product_name = product_info.find("h2",attrs={"class":"product_name"}).getText()
        self.product_description = product_info.find("div",attrs={"class":"long_description"}).getText()
        self.product_price = product_info.select_one('[id="ctl00_MainContent_ProductInfo1_ctl00_HiddenPriceModule1_hidPCPrice"]')['value']
        self.product_url = self.product_url
        self.image_url = 'https://www.arbonne.com'+ product_info.find("img")['data-original']
        if(len(Product.objects.all())>4):
            Product.objects.first().delete()
        return super(Product, self).save(*args, **kwargs)


class Analytics(models.Model):
    hits = models.IntegerField(default=0)
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    last_hit = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username + " hits"

class Hit(models.Model):
    dateOfHit = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " hit at " + str(self.dateOfHit)
