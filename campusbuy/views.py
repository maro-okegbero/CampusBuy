from django.shortcuts import render, render_to_response
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Category, Advert
from django.shortcuts import redirect
from .forms import PostAdForm
from django.contrib.postgres.search import SearchVector


# The view the view baby!

def homepage(request):
    """
    This view is responsible for displaying the contents of the homepage
    :param request:
    :return:
    """
    Categories = Category.objects.all()
    return render(request, 'campusbuy/index.html', {'Categories': Categories})


def viewAd(request, category_name):
    """

    :param request:
    :param category_name:
    :return: All the ads in a named category
    """
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
        return render(request, 'campusbuy/My_Ads.html', context)

    except Category.DoesNotExist:
        raise Http404("Category Does Not Exist")


def postAd(request):
    if request.method == "POST":
        form = PostAdForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.published_date = timezone.now()
            post.save()
            return viewAd(request, category_name=post.category)
        else:
            return render('<h1> Hold on a minute, something went wrong. Try posting again</h1>')

    else:

        form = PostAdForm()
    return render(request, 'campusbuy/new_advert.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    if query:
        results = Advert.objects.annotate(search=SearchVector('Item', 'Description', 'Seller_Name'), ).filter(
            search=query)
    else:
        results = Advert.objects.filter(Seller_Name__startswith="/")

    return render(request, 'campusbuy/search.html', {'results': results})


def handler404(request, exception, template_name="404_Error.html"):
    response = render_to_response("campusbuy/404_Error.html")
    response.status_code = 404
    return response
