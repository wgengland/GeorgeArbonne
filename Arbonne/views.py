from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import timedelta
from .models import Product, Analytics,Hit
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
import requests
from .timer import Timer
# Create your views here.
Arbonne_URL_1 = "https://www.arbonne.com/Pws/"
Arbonne_URL_2 = "/store/AMUK/Catalog/CategoryInfo.aspx?cid="
class IndexView(generic.ListView):
    template_name = 'Arbonne/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:4]

def my_favorites(request,profile_id):
    if Hit.objects.filter(user = profile_id):
        print("user found")
        mostrecenthit = Hit.objects.filter(user = profile_id).order_by('-dateOfHit')[0]
        if timezone.now()-mostrecenthit.dateOfHit>timedelta(seconds=1):
            new_hit = Hit(user = User.objects.get(id=profile_id))
            new_hit.save()

    listings = Product.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:4]
    listings = Product.objects.filter(author_id = profile_id)

    final_postings = []
    for product in listings[:len(listings)]:
        title = product.product_name
        try:
            price = "£"+str(product.product_price)+"0"
        except:
            price = 'Out of Stock'
        description = product.product_description
        link = product.product_url
        image_url = product.image_url
        final_postings.append((title,price,description,link,image_url))
    title_of_page = "View My Shop"
    stuff_for_frontend = {
        'final_postings':final_postings,
        'title_of_page':title_of_page,
        'profile_id':profile_id,

    }
    return render(request,'Arbonne/home.html',stuff_for_frontend)
def skincare(request,profile_id):
    username = User.objects.get(id=profile_id).username
    catalog_url = Arbonne_URL_1 + username + Arbonne_URL_2 + "480&viewall=true"
    stuff_for_frontend = get_stuff_for_front_end(catalog_url,"Skincare")
    stuff_for_frontend['profile_id']=profile_id
    stuff_for_frontend['User']=User.objects.get(id=profile_id)
    return render(request,'Arbonne/home.html',stuff_for_frontend)
def bath_and_body(request,profile_id):
    username = User.objects.get(id=profile_id).username
    catalog_url = Arbonne_URL_1 + username + Arbonne_URL_2 + "481&viewall=true"
    stuff_for_frontend = get_stuff_for_front_end(catalog_url,"Bath And Body")
    stuff_for_frontend['profile_id']=profile_id
    return render(request,'Arbonne/home.html',stuff_for_frontend)
def makeup(request,profile_id):
    username = User.objects.get(id=profile_id).username
    catalog_url = Arbonne_URL_1 + username + Arbonne_URL_2 + "484&viewall=true"
    stuff_for_frontend = get_stuff_for_front_end(catalog_url,"Makeup")
    stuff_for_frontend['profile_id']=profile_id
    return render(request,'Arbonne/home.html',stuff_for_frontend)
def nutrition(request,profile_id):
    username = User.objects.get(id=profile_id).username
    catalog_url = Arbonne_URL_1 + username + Arbonne_URL_2 + "486&viewall=true"
    stuff_for_frontend = get_stuff_for_front_end(catalog_url,"Nutrition")
    stuff_for_frontend['profile_id']=profile_id
    return render(request,'Arbonne/home.html',stuff_for_frontend)
def hair(request,profile_id):
    username = User.objects.get(id=profile_id).username
    catalog_url = Arbonne_URL_1 + username + Arbonne_URL_2 + "482&viewall=true"
    stuff_for_frontend = get_stuff_for_front_end(catalog_url,"Hair")
    stuff_for_frontend['profile_id']=profile_id
    return render(request,'Arbonne/home.html',stuff_for_frontend)
def special_offers(request,profile_id):
    return render(request,'Arbonne/home.html',stuff_for_frontend)


def get_stuff_for_front_end(url_string,search_string):
        # measure process time
    t=Timer()
    t.start()
    response = requests.get(url_string)
    data = response.text
    soup = BeautifulSoup(data,features='html.parser')
    listing_soup = BeautifulSoup(data,features='html.parser')
    listings = listing_soup.find_all("div",class_="grid_item",limit=30)#soup.find_all("div",class_="product_grid")#.find_all("div",class_="grid_item")
    final_postings = []
    for product in listings[:len(listings)]:
        title = product.find("div",class_="product_name").getText()
        try:
            price = product.find("div",class_="PriceRow-Data").getText()
        except:
            price = 'Out of Stock'
        description = product.find("div",class_="short_description").getText()
        #link = product.find('a').get('href')
        link = 'https://www.arbonne.com/Pws/SianHawley/store/AMUK'+product.find('a').get('href')[2:]
        image_url = 'https://www.arbonne.com'+ product.find('img').get('data-original')
        loading = product.find('img').get('src')
        #print(f'\nTitle {title}\nPrice {price}\nDescription {description}\nLink {link}\nImage URL {image_url}\nLoading URL {loading}')
        final_postings.append((title,price,description,link,image_url))
    title_of_page = search_string
    stuff_for_frontend = {
        'final_postings':final_postings,
        'title_of_page':title_of_page,
    }
    t.stop()
    return stuff_for_frontend
