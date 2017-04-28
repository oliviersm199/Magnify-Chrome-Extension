import requests

class GuardianClient:
    api_key = "33923dfd-ff29-4b38-8245-ec52320277c2"
    api_url = "http://content.guardianapis.com/search"

    def __call__(self, keywords):
        '''
        Will return a set of articles organized by headline and url.
        '''
        query = self._construct_guardian_query(keywords)
        answers = self._make_guardian_request(query).json()

        return [{"headline":result['webTitle'],"url":result['webUrl']} for result in answers['response']['results']]

    def _construct_guardian_query(self,keywords):
        '''
        Takes a list of keywords and creates a simple query for Guardian which
        just ORS all the keywords to give the maximum # of articles.
        '''
        return " OR ".join(keywords)

    def _make_guardian_request(self,q):
        '''
        uses requests to construct a single request to the Guardian article search API
        q: represents the query string sent to the guardian API (Apache Lucene Format)

        '''
        return requests.get(self.api_url,params={"api-key":self.api_key,"q":q})
