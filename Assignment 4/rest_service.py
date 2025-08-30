from bs4 import BeautifulSoup
import requests

blacklist = [ # List with elements we don't want to keep
    'script',
    'style',
    'aside'
]

def url_to_string(url):
    request = requests.get(url)
    html = request.text
    soup = BeautifulSoup(html, "html5lib")
    
    for script in soup(blacklist):
        script.extract()
    text = [paragraph.get_text() for paragraph in soup.find_all('p')]
    return " ".join(text)