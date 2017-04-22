from flask import Flask, jsonify,request, abort
import uuid
import datetime
import settings
import natural_language_proc as nlp
from api_integration.ny_times import get_nytimes_article_urls
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World",200


@app.route('/article',methods=["POST"])
def save_article():
    random_file_name = str(uuid.uuid4())
    current_dt = str(datetime.datetime.now())

    page = request.get_data()
    keywords = nlp.get_keywords(page)
    # Save Raw HTML to disk
    #random_file_name = str(uuid.uuid4())
    #html_file_name = "articles/" + random_file_name + "-"  + current_dt + ".html"
    #with open(html_file_name,'w') as filename:
    #    filename.write(page)

    # Retrieve text from file
    ny_times = get_nytimes_article_urls(keywords)
    return jsonify({"id":random_file_name,
                    "datetime":current_dt,
                    "keywords":keywords,
                    "ny_times":ny_times})


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True,threaded=True)
