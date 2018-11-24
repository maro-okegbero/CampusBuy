from django.shortcuts import render

from django.utils import timezone
from .models import Category, Advert
from django.shortcuts import redirect
from .forms import PostAdForm

# Create your views here.

def Homepage(request):
    Categories = Category.objects.all()
    return render(request, 'campusbuy/index.html', {'Categories': Categories} )


def PostAd(request):
        if request.method == "POST":
            form = PostAdForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                post.published_date = timezone.now()
                post.save()
                return redirect('Homepage')

        else:

            form = PostAdForm()
        return render(request, 'campusbuy/new_advert.html', {'form': form})


def ViewAd(request, category_name):
    kategories = Category.objects.all()
    categories = Category.objects.get(Name=category_name)
    return render(request, 'campusbuy/ads.html', {'categories': categories}, {'kategories': kategories})
