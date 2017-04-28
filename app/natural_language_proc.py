import collections
from nltk.corpus import stopwords as the_stop_words
from nltk.tokenize.regexp import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import string
import web_scraping


class NaturalLanguageProcessor:
    stopwords = the_stop_words.words('english')

    def get_keywords(self, text):
        raw = web_scraping.get_text_from_html(text)
        token_words = self.tokenize_text(raw)
        normalized_words = self.normalize_words(token_words)
        ascii_only = self.filter_only_ascii_words(normalized_words)
        lemma_words = self.lemmanize_text(ascii_only)
        key_words = self.remove_english_stop_words(lemma_words)
        document_freq = collections.Counter(key_words)
        return [ keyword[0] for keyword in document_freq.most_common(10) ]

    def tokenize_text(self, text):
        words = WordPunctTokenizer().tokenize(text)
        return words

    def remove_english_stop_words(self, words):
        return [w for w in words if w.lower() not in self.stopwords]

    def normalize_words(self,text):
        return sorted([w.lower() for w in text])

    def filter_punctuation(self, text):
        punctuation_filter = "^[" + string.punctuation + "]$"
        return [w for w in text if re.search(punctuation_filter,w)]

    def filter_only_ascii_words(self, text):
        contains_words_filter = "^[" + string.ascii_lowercase + "]+$"
        return [w for w in text if re.search(contains_words_filter,w)]

    def lemmanize_text(self, tokens):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in tokens]
