from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


def esearch(size, search_query="", not_include=""):
    es = Elasticsearch()
    q = Q("bool", should=[Q("match", content=search_query),
                          Q({"match": {"content": {"query": search_query, "operator": "and"}}}),
                          Q({"match_phrase": {"content": {"query": search_query, "boost": 2}}})],
          must_not=[Q("match", content=not_include)])
    s = Search(using=es, index="article").query(q)[:size]
    response = s.execute()
    print('Total', response.hits.total, ' hits found.')
    results = get_results(response)
    return (results, response.hits.total['value'])


def get_results(response):
    results = []
    for i, result in enumerate(response):
        result_tuple = (i+1, result.meta.score, result.headline,
                        result.author, result.date,
                        result.content, result.link)
        results.append(result_tuple)
    return results