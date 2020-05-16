from django.urls import path
from .views import ProductCreateView,ProductUpdateView,analyticsview,analyticsdata

app_name = 'users'
urlpatterns = [
    path('create_product/',ProductCreateView.as_view(),name = 'create_product'),
    path('update_product/<int:pk>/',ProductUpdateView.as_view(),name = 'update_product'),
    path('analytics_view/',analyticsview,name = 'analytics_view'),
    path('analyticsdata/',analyticsdata,name='analyticsdata')
#path('login/',login)
]
