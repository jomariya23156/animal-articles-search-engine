from django.shortcuts import render
from django.http import HttpResponse
from .es_call import esearch


def search_index(request):
    results = []
    search_query_term = ""
    not_include_term = ""
    size_term = 10
    if request.GET.get('search_query') and request.GET.get('not_include') and request.GET.get('size'):
        search_query_term = request.GET['search_query']
        not_include_term = request.GET['not_include']
        size_term = int(request.GET['size'])
    elif request.GET.get('search_query') and request.GET.get('not_include'):
        search_query_term = request.GET['search_query']
        not_include_term = request.GET['not_include']
    elif request.GET.get('search_query') and request.GET.get('size'):
        search_query_term = request.GET['search_query']
        size_term = int(request.GET['size'])
    elif request.GET.get('search_query'):
        search_query_term = request.GET['search_query']
    elif request.GET.get('not_include'):
        not_include_term = request.GET['not_include']
    elif request.GET.get('size'):
        size_term = int(request.GET['size'])
    search_term = search_query_term or not_include_term or size_term
    (results, total_hits) = esearch(size_term, search_query=search_query_term, not_include=not_include_term)
    print(results)
    context = {'results': results, 'matched': total_hits, 'showing': len(results), 'search_term': search_term}
    return render(request, 'esearch/main.html', context)

# Create your views here.
