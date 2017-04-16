import nltk
from nltk.corpus import stopwords as the_stop_words
from nltk.tokenize.regexp import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter
import math
import re
import string
import web_scraping

stopwords = the_stop_words.words('english')

def tokenize_text(text):
    words = WordPunctTokenizer().tokenize(text)
    return words

def remove_english_stop_words(words):
    return [w for w in words if w.lower() not in stopwords]

def normalize_words(text):
    return sorted([w.lower() for w in text])

def filter_punctuation(text):
    punctuation_filter = "^[" + string.punctuation + "]$"
    return [w for w in text if re.search(punctuation_filter,w)]

def filter_only_ascii_words(text):
    contains_words_filter = "^[" + string.ascii_lowercase + "]+$"
    return [w for w in text if re.search(contains_words_filter,w)]

def lemmanize_text(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]


def get_keywords(text):
    raw = web_scraping.get_text_from_html(text)
    token_words = tokenize_text(raw)
    normalized_words = normalize_words(token_words)
    ascii_only = filter_only_ascii_words(normalized_words)
    lemma_words = lemmanize_text(ascii_only)
    key_words = remove_english_stop_words(lemma_words)
    document_freq = Counter(key_words)
    return [ keyword[0] for keyword in document_freq.most_common(10) ]
