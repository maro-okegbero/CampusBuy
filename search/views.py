from django.shortcuts import render

from search.documents import PostDocument




def search(request):
    q = request.GET.get('q')
    if q:
        adverts = PostDocument.search().query("match", Item=q,)
    else:
        adverts = ''

    return render(request, 'search/search_page.html', {'adverts': adverts})