import requests

class PageReader:
    def __init__(self):
        self.URL_lambda = lambda pageNr : f"https://jsonmock.hackerrank.com/api/articles?page={pageNr}"
        self.session = requests.Session()
        self.pages_data = []
        self.page_number = 0
    
    """
    Gets page data on given pageNr
    """
    def get_current_page(self):
        return (self.session
                .get(self.URL_lambda(self.page_number))
                .json())['data']

    """
    Updates the total pages count
    """
    def get_total_pages(self):
        return (self.session
                .get(self.URL_lambda(1))
                .json())['total_pages']
    
    """
    Updates the total pages number and yields the remaining pages.
    """
    def yield_remaining_pages(self):
        total_pages = self.get_total_pages()
        while self.page_number < total_pages:
            self.page_number += 1
            yield self.get_current_page()
    
    """
    Updates pages data list.
    """
    def update_pages_data(self):
        for page in self.yield_remaining_pages():
            self.pages_data += page
    
    """
    Returns updated pages data list.
    """
    def get_updated_pages_data(self):
        self.update_pages_data()
        return self.pages_data