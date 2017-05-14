import api_integration.ny_times as ny_times
import api_integration.guardian as guardian
import api_integration.hacker_news as hn

api_integrations = {"ny_times":ny_times.NYTimesClient,
                    "guardian":guardian.GuardianClient,
                    "hackernews":hn.HackerNewsClient}


def get_articles(keywords):
    '''
    Iterates through each supported api integration and constructs a
    key value pair of all api integrations
    '''
    return { key:api_integrations[key]()(keywords) for key in api_integrations}
