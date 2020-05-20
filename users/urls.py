from django.urls import path
from .views import ProductCreateView,ProductUpdateView,analyticsview,analyticsdata,ContactInfoUpdateView,analyticsdatadrilldown

app_name = 'users'
urlpatterns = [
    path('create_product/',ProductCreateView.as_view(),name = 'create_product'),
    path('update_product/<int:pk>/',ProductUpdateView.as_view(),name = 'update_product'),
    path('update_contact_info/<int:pk>/',ContactInfoUpdateView.as_view(),name = 'update_contact_info'),
    path('analytics_view/',analyticsview,name = 'analytics_view'),
    path('analyticsdata/',analyticsdata,name='analyticsdata'),
    path('analyticsdatadrilldown/',analyticsdatadrilldown,name='analyticsdatadrilldown')


#path('login/',login)
]
