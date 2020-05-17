from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Arbonne.models import Product
from django.shortcuts import redirect
from django.views.generic import CreateView,UpdateView
from Arbonne.models import Product,Analytics,Hit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils import timezone

import datetime
# Create your views here.
def login(request):
    return render(request,'users/login.html')

@login_required
def profile(request):
    if(len(Product.objects.filter(author_id = request.user.id))>4):
        products = Product.objects.all()
        for product in products[0:1]:
            product.delete()
    user_home_url = "https://geobonne.herokuapp.com/"+str(request.user.id)
    postings_by_user = Product.objects.filter(author_id = request.user.id)
    stuff_for_frontend = {
        'user_home_url':user_home_url,
        'postings_by_user':postings_by_user,
    }
    if Hit.objects.filter(user_id = request.user.id):
        renderhits=True
        stuff_for_frontend['renderhits']=renderhits
    return render(request, 'users/profile.html',stuff_for_frontend)

@login_required
def analyticsview(request):
    stuff_for_frontend = {
    }
    return render(request,'users/analytics.html',stuff_for_frontend)

class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    template_name = 'users/create_product_form.html'
    fields = ['product_url']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    template_name = 'users/update_product_form.html'
    fields = ['product_url']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def analyticsdata(request):

    if Hit.objects.filter(user_id = request.user.id):
        analyticsdata = []
        hits=Hit.objects.filter(user_id=request.user.id).order_by('-dateOfHit')
        print(hits)
        largestweek = int((timezone.now()-hits[len(hits)-1].dateOfHit).days/7)
        print(largestweek)
        data={}
        for hit in hits:
            print(hit.dateOfHit)
            weekofhit = largestweek - int((timezone.now()-hit.dateOfHit).days/7)
            if "week" + str(weekofhit) not in data.keys():
                data["week" + str(weekofhit)]=0
            data["week" + str(weekofhit)]= data["week" + str(weekofhit)]+1
            print(data)

        for i in range(largestweek+1):
            if "week" + str(i) not in data.keys():
                analyticsdata.append({'week '+str(i):0})
            else:
                analyticsdata.append({'week '+str(i):data['week'+str(i)]})
        print(analyticsdata)
        return JsonResponse(analyticsdata,safe=False)
    else:
        return None
