from flask import Flask, jsonify,request, abort
import uuid
import datetime
import settings
import natural_language_proc as nlp
import api_integration.ny_times
import api_integration.article_accumulator as article_a
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World",200


@app.route('/article',methods=["POST"])
def process_article():

    # generate a random file name and a current datetime
    random_file_name = str(uuid.uuid4())
    current_dt = str(datetime.datetime.now())

    page = request.get_data()

    # push page text through nlp pipeline
    processor = nlp.NaturalLanguageProcessor()
    keywords = processor.get_keywords(page)


    return_dict = {"id":random_file_name,
                    "datetime":current_dt,
                    "keywords":keywords}

    api_results = article_a.get_articles(keywords)

    for result in api_results.keys():
        return_dict[result] = api_results[result]

    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True,threaded=True)
