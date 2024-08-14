import unittest
import requests

# https://www.geeksforgeeks.org/python-import-from-parent-directory/
import sys
import os
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

import page_reader

class TestPageReader(unittest.TestCase):

    """
    Tests page_reader.PageReader()
    """
    def test_init(self):
        pr = page_reader.PageReader()
        self.assertEqual(
            pr.URL_lambda(1),
            "https://jsonmock.hackerrank.com/api/articles?page=1",
            "Test PageReader URL_lambda"
        )
        self.assertEqual(
            type(pr.session),
            requests.Session,
            "Test if a requests session is open"
        )
        self.assertEqual(
            pr.pages_data,
            [],
            "Test if pages_data is initialized"
        )
        self.assertEqual(
            pr.page_number,
            0,
            "Test if page_number is initialized"
        )
    
    """
    Tests page_reader.PageReader().get_current_page()
    """
    def test_get_current_page(self):
        pr = page_reader.PageReader()

        pr.page_number = 1
        page1 = (requests
                .get("https://jsonmock.hackerrank.com/api/articles?page=1")
                .json())['data']
        self.assertEqual(
            pr.get_current_page(),
            page1,
            "Test if get_current_page() returns correct page."
        )

        pr.page_number += 1
        page2 = (requests
                .get("https://jsonmock.hackerrank.com/api/articles?page=2")
                .json())['data']
        self.assertEqual(
            pr.get_current_page(),
            page2,
            "Test if get_current_page() returns correct page."
        )

    """
    Tests page_reader.PageReader().get_total_pages()
    """
    def test_get_total_pages(self):
        total_pages = (requests
                       .get("https://jsonmock.hackerrank.com/api/articles?page=1")
                       .json())['total_pages']
        self.assertEqual(
            page_reader.PageReader().get_total_pages(),
            total_pages,
            "Test if get_total_pages() works correctly"
        )
    
    """
    Tests page_reader.PageReader().yield_remaining_pages()
    """
    def test_yield_remaining_pages(self):
        pr = page_reader.PageReader()
        pages = []
        for page in pr.yield_remaining_pages():
            pages.append(page)
        length1 = len(pages)
        pageNr1 = pr.page_number

        for page in pr.yield_remaining_pages():
            pages.append(page)
        length2 = len(pages)
        pageNr2 = pr.page_number

        self.assertEqual(
            length2 - length1,
            pageNr2 - pageNr1,
            "Test that yield_remaining_pages() adds the same amount of elements as page number increases"
        )

        self.assertEqual(
            pr.get_total_pages(),
            pageNr2,
            "Test that page_number is same as total_pages (if new pages are added, between this assertion and the call of yield_remaining_pages(), the test should fail)"
        )
    
    """
    Tests page_reader.PageReader().update_pages_data()
    """
    def test_update_pages_data(self):
        
        with self.assertRaises(
            AssertionError,
            msg="Test wrong type of function"):
            page_reader.PageReader(process_function="e")
        
        pr = page_reader.PageReader(process_function=lambda page: [e["title"] for e in page])

        pr.update_pages_data()
        length1 = len(pr.pages_data)
        pageNr1 = pr.page_number
        
        pr.update_pages_data()
        length2 = len(pr.pages_data)
        pageNr2 = pr.page_number

        self.assertEqual(
            length2 - length1,
            pageNr2 - pageNr1,
            "Test that update_pages_data() adds the same amount of elements as page number increases"
        )

        self.assertEqual(
            pr.get_total_pages(),
            pageNr2,
            "Test that page_number is same as total_pages (if new pages are added, between this assertion and the call of yield_remaining_pages(), the test should fail)"
        )

        with self.assertRaises(
            AttributeError,
            msg="Test that process_function works correctly"):
            pr.pages_data[0].keys()
    
    """
    Tests page_reader.PageReader().get_pages_data()
    """
    def test_get_pages_data(self):
        pr = page_reader.PageReader()
        pr.update_pages_data()
        self.assertEqual(
            pr.get_pages_data(),
            pr.pages_data,
            "Tests that get_pages_data() returns correct value"
        )


if __name__ == '__main__':
    unittest.main()