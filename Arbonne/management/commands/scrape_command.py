from django.core.management.base import BaseCommand
from selenium import webdriver
from Arbonne.models import Product
from django.utils import timezone

class Command(BaseCommand):
    help = 'Update Product List'

    def handle(self,*args,**kwargs):
        browser = webdriver.Chrome()
        browser.get('https://www.arbonne.com/Pws/SianHawley/store/AMUK/catalog/Nutrition,486.aspx')
        testprod = Product(product_name='test',product_description='testing des',price=1.50,pub_date=timezone.now())
        testprod.save()
'''
from models import Product
from django.conf import settings

from django.utils import timezone
testproduct = Product(product_name='test1',product_description='test description',price='1.50',pub_date=timezone.now())
testproduct.save()
browser = webdriver.Chrome()
print(type(browser))
browser.get('https://www.arbonne.com/Pws/SianHawley/store/AMUK/catalog/Nutrition,486.aspx')
    '''
