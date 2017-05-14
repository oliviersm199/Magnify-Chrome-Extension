import requests
import xmltodict
import json

class HackerNewsClient:
    api_url = "https://hnrss.org/newest"

    def __call__(self, keywords):
        '''
        Will return a set of articles organized by headline and url.
        '''
        query = self._construct_hackernews_query(keywords)
        answers = self._make_hackernews_request(query)

        news_dict = xmltodict.parse(answers.content)

        try:
            return [{"headline":item['title'],"url":item['link']} for item in news_dict['rss']['channel']['item']]
        except KeyError as e:
            print(answers)

    def _construct_hackernews_query(self,keywords):
        '''
        Takes a list of keywords and creates a simple query for hackernews which
        just ORS all the keywords to give the maximum # of articles.
        '''
        return " OR ".join(keywords)

    def _make_hackernews_request(self,q):
        '''
        uses requests to construct a single request to the hackernews article search API
        q: represents the query string sent to the hackernews API (Apache Lucene Format)

        '''
        return requests.get(self.api_url,params={"q":q})
