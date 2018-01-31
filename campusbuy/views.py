from django.shortcuts import render

# Create your views here.

def advert_list(request):
    return render(request, 'campusbuy/index.html')
