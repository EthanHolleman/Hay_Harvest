import requests
from bs4 import BeautifulSoup
from Article import Article

class Listing_Page():

    def __init__(self, url, headers=None, request=None, soup=None):
        self.url = url
        self.headers = headers
        self.request = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.request.content, 'html.parser')
        self.listings = self.soup.find_all('article')
        self.articles = [Article(article_html) for article_html in self.listings]

    def print_listings(self):
        for a in self.articles:
            print(a)
