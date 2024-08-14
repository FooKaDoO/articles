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
    Tests page_reader.get_pages_data()
    """
    def test_get_pages_data(self):
        self.assertTrue(
            isinstance(page_reader.get_pages_data(), list),
            "Test if page_reader.get_pages_data() returns a list."
        )
        for elem in page_reader.get_pages_data():
            self.assertTrue(
                isinstance(elem, dict),
                "Test if page_reader.get_pages_data() returns a list of dictionary objects."
            )
            self.assertTrue(
                isinstance(elem["title"], str),
                "Test if page_reader.get_pages_data() returns a list of dictionary objects with keys 'title': str and 'num_comments': int."
            )
            self.assertTrue(
                isinstance(elem["num_comments"], int),
                "Test if page_reader.get_pages_data() returns a list of dictionary objects with keys 'title': str and 'num_comments': int."
            )


if __name__ == '__main__':
    unittest.main()