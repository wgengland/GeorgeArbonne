from django.contrib import admin
from .models import Product, Analytics,Hit,BlogPost
# Register your models here.


admin.site.register(Product)
admin.site.register(Analytics)
admin.site.register(Hit)
admin.site.register(BlogPost)
