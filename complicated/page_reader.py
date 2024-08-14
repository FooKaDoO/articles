import requests

class PageReader:
    
    def __init__(self, URL_lambda):
        self.URL_lambda = URL_lambda
        self.session = requests.Session()
        self.pages_data = []
        self.page_number = 0
    
    """
    Gets page data on given pageNr
    """
    def get_page(self, pageNr: int):
        return (self.session
                .get(self.URL_lambda(pageNr))
                .json())['data']
    
    """
    Gets page data on previous page
    """
    def go_to_previous_page(self):
        self.page_number -= 1
        return self.get_page(self.page_number)

    """
    Gets page data on next page
    """
    def go_to_next_page(self):
        self.page_number += 1
        return self.get_page(self.page_number)

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
            yield self.go_to_next_page()
    
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