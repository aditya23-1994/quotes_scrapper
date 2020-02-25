from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def quotes(self):
        locators = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locators)
        return [QuoteParser(e) for e in quote_tags]