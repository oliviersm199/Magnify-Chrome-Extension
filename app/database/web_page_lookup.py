from mongo_database_client import db
import user
import web_page
from bson.son import SON


def create_webpage_lookup(user_id, webpage, lookup_id, filename, keywords, datetime, articles):
    # get a user object or create one
    check_user = user.get_user(user_id)
    if not check_user:
        check_user = user.create_user(user_id)

    # create a webpage object
    webpage_id = web_page.put(webpage, filename)

    webpage_lookup = {"user": check_user,
                      "webpage": webpage_id,
                      "keywords": keywords,
                      "datetime": datetime,
                      "lookup_id": lookup_id,
                      "articles": articles}

    return db.webpage_lookup.insert_one(webpage_lookup)

def get_webpage_lookup(lookup_id):
    return db.webpage_lookup.find_one({"lookup_id": lookup_id})

def count_keywords(user):
    '''
    Will get a particular users favorite keywords using MongoDB aggregation framework
    '''
    pipeline = [{"$match":{"user":user}},
                {"$unwind": "$keywords"},
                {"$group": {"_id": "$keywords", "count": {"$sum": 1}}},
                {"$sort": SON([("count", -1), ("_id", -1)])}]
    keywords_list = list(db.webpage_lookup.aggregate(pipeline))
    formatted_list = [{"count":freq_word['count'],"word": freq_word['_id']}  for freq_word in keywords_list]
    return formatted_list
