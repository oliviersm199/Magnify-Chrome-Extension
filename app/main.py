from flask import Flask, jsonify, request, abort
import uuid
import datetime
import settings
import natural_language_proc as nlp
import api_integration.ny_times
import api_integration.article_accumulator as article_a
import database.web_page_lookup as web_page_lookup
import database.user as user_collection

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World", 200


@app.route('/article', methods=["POST"])
def process_article():
    # generate a random file name and a current datetime

    lookup_id = str(uuid.uuid4())
    current_dt = datetime.datetime.now()
    filename = lookup_id + str(current_dt) + ".txt"
    content = request.form['page']
    user_id = request.form['user_id']

    # push page text through nlp pipeline
    processor = nlp.NaturalLanguageProcessor()
    keywords = processor.get_keywords(content)

    # Add results as a record to database.
    api_results = article_a.get_articles(keywords)
    webpage_lookup = web_page_lookup.create_webpage_lookup(user_id,
                                                         content,
                                                         lookup_id,
                                                         filename,
                                                         keywords,
                                                         current_dt,
                                                         api_results)

    # Get the User Object and find the top 10 keywords
    user = user_collection.get_user(user_id)
    user_keywords = web_page_lookup.count_keywords(user)[:10]

    return_dict = {"lookup_id": lookup_id,
                   "user_id": user_id,
                   "datetime": str(current_dt),
                   "keywords": keywords,
                   "user_keywords":user_keywords}

    for result in api_results.keys():
        return_dict[result] = api_results[result]

    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
