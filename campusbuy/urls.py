from django.urls import path
from .import views
urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Post_Ad', views.PostAd, name='PostAd')

]
