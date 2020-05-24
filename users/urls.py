from django.urls import path
from .views import ProductCreateView,ProductUpdateView,analyticsview,analyticsdata,ContactInfoUpdateView,analyticsdatadrilldown,BlogPostCreateView,BlogPostUpdateView,BlogPostDeleteView

app_name = 'users'
urlpatterns = [
    path('create_product/',ProductCreateView.as_view(),name = 'create_product'),
    path('update_product/<int:pk>/',ProductUpdateView.as_view(),name = 'update_product'),
    path('update_contact_info/<int:pk>/',ContactInfoUpdateView.as_view(),name = 'update_contact_info'),
    path('analytics_view/',analyticsview,name = 'analytics_view'),
    path('analyticsdata/',analyticsdata,name='analyticsdata'),
    path('analyticsdatadrilldown/',analyticsdatadrilldown,name='analyticsdatadrilldown'),
    path('create_blog_post/',BlogPostCreateView.as_view(),name = 'create_blog_post'),
    path('update_blog_post/<int:pk>/',BlogPostUpdateView.as_view(),name = 'update_blog_post'),
    path('delete_blog_post/<int:pk>/',BlogPostDeleteView.as_view(),name = 'delete_blog_post')


#path('login/',login)
]
