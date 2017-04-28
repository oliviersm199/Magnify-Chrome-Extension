import requests

class NYTimesClient:
    api_key = "a1461f82f3954f03a8c4e4528d53cf23"
    api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

    def __call__(self, keywords):
        '''
        Will return a set of articles organized by headline and url.
        '''
        query = self._construct_nytimes_query(keywords)
        answers = self._make_nytimes_request(query).json()
        return [{"headline":result['headline']['main'],"url":result['web_url']} for result in answers['response']['docs']]

    def _construct_nytimes_query(self,keywords):
        '''
        Takes a list of keywords and creates a simple query for NY_Times which
        just ORS all the keywords to give the maximum # of articles.
        '''
        return " OR ".join(keywords)

    def _make_nytimes_request(self,q):
        '''
        uses requests to construct a single request to the NY Times article search API
        q: represents the query string sent to the NYTimes API (Apache Lucene Format)

        '''
        return requests.get(self.api_url,params={"api-key":self.api_key,"q":q})
