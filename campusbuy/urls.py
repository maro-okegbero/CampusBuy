from django.urls import path
from .import views
from campusbuy.models import Category, Advert
urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Post_Ad', views.PostAd, name='PostAd'),
    path('search', views.search, name='search'),
    path('<category_name>', views.ViewAd, name='ViewAd'),



]


