import requests
import data_parser

def get_pages_data():
    pages_data = []

    page_number = 0
    total_pages = 1
    
    session = requests.Session()

    while page_number < total_pages:
        page_number += 1
        res = (session
               .get(f"https://jsonmock.hackerrank.com/api/articles?page={page_number}")
               .json())
        data, total_pages = res["data"], res["total_pages"]
        pages_data += data_parser.process_page(data)

    return pages_data