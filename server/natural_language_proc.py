from nltk.corpus import stopwords as the_stop_words
from nltk.tokenize.regexp import WordPunctTokenizer


stopwords = the_stop_words.words('english')

def tokenize_text(text):
    words = WordPunctTokenizer().tokenize(text)
    return words

def remove_english_stop_words(words):
    return [w for w in words if w.lower() not in stopwords]
