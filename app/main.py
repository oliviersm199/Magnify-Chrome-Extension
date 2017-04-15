from flask import Flask, jsonify,request, abort
import uuid
import datetime
import web_scraping
import settings
import natural_language_proc as nlp
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World",200


@app.route('/article',methods=["POST"])
def save_article():
    random_file_name = str(uuid.uuid4())
    current_dt = str(datetime.datetime.now())

    page = request.get_data()

    # Save Raw HTML to disk
    random_file_name = str(uuid.uuid4())
    html_file_name = "articles/" + random_file_name + "-"  + current_dt + ".html"
    with open(html_file_name,'w') as filename:
        filename.write(page)

    # Retrieve text from file,
    text_file = web_scraping.get_text_from_html(page)
    token_words = nlp.tokenize_text(text_file)
    key_words = nlp.remove_english_stop_words(token_words)

    return jsonify({"id":random_file_name,
                    "datetime":current_dt,
                    "key_words":key_words,
                    "token_words":token_words})



# @app.errorhandler(404)
# def page_not_found(error):
# 	app.logger.error('Page not found: %s', (request.path))
# 	return jsonify({"error":"Not found","code":404})
#
#
# @app.errorhandler(500)
# def internal_server_error(error):
#     app.logger.error('Server Error: %s', (error))
#     return jsonify({"error":"Server Error","code":500})
#
# @app.errorhandler(Exception)
# def unhandled_exception(e):
#     app.logger.error('Unhandled Exception: %s', (e))
#     return jsonify({"error":"Server Error","code":500})


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True,threaded=True)
