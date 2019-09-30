from django.urls import path
from .import views
from campusbuy.models import Category, Advert
urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('Post_Ad', views.postAd, name='PostAd'),
    path('search', views.search, name='search'),
    path('<category_name>', views.viewAd, name='ViewAd'),



]


