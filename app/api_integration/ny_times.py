import requests

article_search_api_key = "a1461f82f3954f03a8c4e4528d53cf23"


url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"



def construct_nytimes_query(keywords):
    query_string = ""
    for itr,word in enumerate(keywords):
        query_string += word
        if itr != len(keywords) - 1:
            query_string += " OR "
    return query_string


def make_nytimes_request(q,url):
    params = {"api-key":article_search_api_key,
              "q":q}
    r = requests.get(url,params=params)
    return r


def get_nytimes_article_urls(keywords):
    answers = make_nytimes_request(construct_nytimes_query(keywords),url).json()
    return [{"headline":result['headline']['main'],"url":result['web_url']} for result in answers['response']['docs']]
