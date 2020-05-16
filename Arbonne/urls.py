from django.urls import path
from . import views
from Arbonne.views import my_favorites,skincare,bath_and_body,makeup,nutrition,hair,special_offers,hair
from django.contrib.auth import views as auth_views

app_name = 'Arbonne'

urlpatterns = [
path('<int:profile_id>/',my_favorites,name = 'my_favorites'),
path('<int:profile_id>/Arbonne/Skincare/',skincare,name = 'skincare'),
path('<int:profile_id>/Arbonne/BathAndBody',bath_and_body,name = 'bath_and_body'),
path('<int:profile_id>/Arbonne/Makeup',makeup,name = 'makeup'),
path('<int:profile_id>/Arbonne/Nutrition',nutrition,name = 'nutrition'),
path('<int:profile_id>/Arbonne/Hair',hair,name = 'hair'),
path('<int:profile_id>/Arbonne/SpecialOffers',special_offers,name = 'special_offers'),
path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

]
