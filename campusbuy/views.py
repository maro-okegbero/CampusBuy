from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Category, Advert
from django.shortcuts import redirect
from .forms import PostAdForm
from django.contrib.postgres.search import SearchVector



# Create your views here.

def Homepage(request):
    Categories = Category.objects.all()
    return render(request, 'campusbuy/index.html', {'Categories': Categories} )




def ViewAd(request, category_name):
    try:
        kategory = Category.objects.get(Name=category_name)
        MyList = kategory.advert_set.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(MyList, 4)
        try:
            AdList = paginator.page(page)
        except PageNotAnInteger:
            AdList = paginator.page(1)
        except EmptyPage:
            AdList = paginator.page(paginator.num_pages)
        context = {'category': category_name, 'categories': AdList}
        return render(request, 'campusbuy/my_ads.html', context)

    except Category.DoesNotExist:
        raise Http404("Category Does Not Exist")



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


def Search(request):
    query = request.GET.get('q')
    if query:
        results = Advert.objects.annotate(search=SearchVector('Item', 'Description', 'Seller_Name'),).filter(search = query)
    else:
        results = Advert.objects.all()

    return render(request, 'campusbuy/search.html', {'results': results})