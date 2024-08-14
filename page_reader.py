import requests
import types

class PageReader:
    """
    process_function takes in a list of elements and 
    must return a list of elements.
    """
    def __init__(self, process_function: types.FunctionType=lambda page : page):
        assert isinstance(process_function, types.FunctionType)
        self.process_function = process_function
        self.URL_lambda = lambda pageNr : f"https://jsonmock.hackerrank.com/api/articles?page={pageNr}"
        self.session = requests.Session()
        self.pages_data = []
        self.page_number = 0
    
    """
    Returns page data on current page number.
    """
    def get_current_page(self):
        return (self.session
                .get(self.URL_lambda(self.page_number))
                .json())['data']

    """
    Returns total pages count.
    """
    def get_total_pages(self):
        return (self.session
                .get(self.URL_lambda(1))
                .json())['total_pages']
    
    """
    Using total pages count, sends requests
    for each remaining page starting from
    self.page_number
    and yields the pages' data.
    """
    def yield_remaining_pages(self):
        total_pages = self.get_total_pages()
        while self.page_number < total_pages:
            self.page_number += 1
            yield self.get_current_page()

    """
    Appends new pages to self.pages_data.
    Uses self.process_function to process data.

    Function returns self
    """
    def update_pages_data(self):
        for page in self.yield_remaining_pages():
            self.pages_data += self.process_function(page)
        return self
    
    """
    Returns pages data.
    """
    def get_pages_data(self):
        return self.pages_data