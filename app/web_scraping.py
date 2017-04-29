from bs4 import BeautifulSoup
from os.path import basename

def get_text_from_html(html):
    # Use beautiful soup to parse through and find "Visible text"
    soup = BeautifulSoup(html,"html.parser")
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title','img'])]
    visible_text = soup.get_text()
    return visible_text
