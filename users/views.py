from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Arbonne.models import Product
from django.shortcuts import redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from Arbonne.models import Product,Analytics,Hit,BlogPost
from .models import ContactInfo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.utils import timezone


import datetime
# Create your views here.
def login(request):
    return render(request,'users/login.html')

@login_required
def profile(request):
    domain=request.build_absolute_uri('/')[:-1]
    if(len(Product.objects.filter(author_id = request.user.id))>4):
        products = Product.objects.all()
        for product in products[0:1]:
            product.delete()
    user_home_url = domain + "/"+str(request.user.id)
    postings_by_user = Product.objects.filter(author_id = request.user.id)
    stuff_for_frontend = {
        'user_home_url':user_home_url,
        'postings_by_user':postings_by_user,
    }
    if Hit.objects.filter(user_id = request.user.id):
        renderhits=True
        stuff_for_frontend['renderhits']=renderhits
    if ContactInfo.objects.filter(user_id = request.user.id):
        stuff_for_frontend['contactinfopk']=ContactInfo.objects.filter(user_id=request.user.id)[0].pk
    else:
        ContactInfo(user=request.user).save()
        stuff_for_frontend['contactinfopk']=ContactInfo.objects.filter(user_id=request.user.id)[0].pk
    if BlogPost.objects.filter(author = request.user):
        BlogPosts=BlogPost.objects.filter(author_id=request.user.id)
        stuff_for_frontend['BlogPosts']=BlogPosts
    print()
    return render(request, 'users/profile.html',stuff_for_frontend)

@login_required
def analyticsview(request):
    stuff_for_frontend = {
    }
    return render(request,'users/analytics.html',stuff_for_frontend)

class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    initial = {'product_url': 'Paste from your Arbonne site'}
    template_name = 'users/create_product_form.html'
    fields = ['product_url']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Product
    template_name = 'users/update_product_form.html'
    fields = ['product_url']
    def get_queryset(self):
        qs = super(ProductUpdateView, self).get_queryset()
        return qs.filter(author=self.request.user)
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        product=self.get_object()
        if self.request.user==product.author:
            return True
        return False


@login_required
def analyticsdata(request):

    if Hit.objects.filter(user_id = request.user.id):
        analyticsdata = []
        hits=Hit.objects.filter(user_id=request.user.id).order_by('-dateOfHit')
        #print(hits)
        largestweek = int((timezone.now()-hits[len(hits)-1].dateOfHit).days/7)
        #print(largestweek)
        data={}
        for hit in hits:
            #print(hit.dateOfHit)
            weekofhit = largestweek - int((timezone.now()-hit.dateOfHit).days/7)
            if "week" + str(weekofhit) not in data.keys():
                data["week" + str(weekofhit)]=0
            data["week" + str(weekofhit)]= data["week" + str(weekofhit)]+1
            #print(data)

        for i in range(largestweek+1):
            if "week" + str(i) not in data.keys():
                analyticsdata.append({'week '+str(i):0})
            else:
                analyticsdata.append({'week '+str(i):data['week'+str(i)]})
        #print(analyticsdata)
        return JsonResponse(analyticsdata,safe=False)
    else:
        return None
@login_required
def analyticsdatadrilldown(request):

    if Hit.objects.filter(user_id = request.user.id):
        analyticsdata = []
        hits=Hit.objects.filter(user_id=request.user.id).order_by('-dateOfHit')
        #print(hits)
        largestweek = int((timezone.now()-hits[len(hits)-1].dateOfHit).days/7)
        #print(largestweek)
        data={}
        for hit in hits:
            #print(hit.dateOfHit)
            weekofhit = largestweek - int((timezone.now()-hit.dateOfHit).days/7)
            if "week" + str(weekofhit) not in data.keys():
                data["week" + str(weekofhit)]=0
            data["week" + str(weekofhit)]= data["week" + str(weekofhit)]+1
            #print(data)

        for i in range(largestweek+1):
            if "week" + str(i) not in data.keys():
                analyticsdata.append({'week '+str(i):0})
            else:
                analyticsdata.append({'week '+str(i):data['week'+str(i)]})
        #print(analyticsdata)
        return JsonResponse(analyticsdata,safe=False)
    else:
        return None

class ContactInfoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = ContactInfo
    template_name = 'users/update_ContactInfo_form.html'
    fields = ['phonenumber','instagram_url']
    success_url='/profile'
    def get_queryset(self):
        qs = super(ContactInfoUpdateView, self).get_queryset()
        return qs.filter(user_id=self.request.user.id)
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        contact_info=self.get_object()
        if self.request.user==contact_info.user:
            return True
        return False

class BlogPostCreateView(LoginRequiredMixin,CreateView):
    model = BlogPost
    initial = {'image_url': 'Find any image on the internet, right click, select "Copy Image Link" or "Copy Image Address", then paste in here'}
    template_name = 'users/create_blog_post_form.html'
    fields = ['blog_post_title','blog_post_content','image_url']
    success_url='/profile'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogPostUpdateView(LoginRequiredMixin,UpdateView):
    model = BlogPost
    template_name = 'users/update_blog_post_form.html'
    fields = ['blog_post_title','blog_post_content','image_url']
    success_url='/profile'
    def get_queryset(self):
        qs = super(BlogPostUpdateView, self).get_queryset()
        return qs.filter(author=self.request.user)
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class BlogPostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = BlogPost
    template_name = 'users/blog_post_confirm_delete.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
