import unittest
import random

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

import data_parser

class TestDataParser(unittest.TestCase):

    """
    Tests data_parser.get_title(article)
    """
    def test_get_title(self):
        list_of_assertions = [
            ({}, None, "Test empty article"),
            ({"title": "some_title"}, "some_title", "Test only title in article"),
            ({"story_title": "some_title"}, "some_title", "Test only story title article"),
            ({"title": 1, "story_title": 1}, None, "Test wrong type title and story_title"),
            ({"title": 1, "story_title": "some_title"}, "some_title", "Test wrong type title"),
            ({"title": "some_title", "story_title": 1}, "some_title", "Test wrong type story_title")
        ]
        for article, return_Val, msg in list_of_assertions:
            self.assertEqual(data_parser.get_title(article), return_Val, msg)
        with self.assertRaises(
            AssertionError,
            msg="Test wrong type of data"):
            data_parser.get_title(5)
    
    """
    Tests data_parser.get_num_comments(article)
    """
    def test_get_num_comments(self):
        list_of_assertions = [
            ({}, 0, "Test empty article"),
            ({"num_comments": 5}, 5, "Test num_comments correct"),
            ({"num_comments": "not_string"}, 0, "Test num_comments wrong type")
        ]
        for article, return_Val, msg in list_of_assertions:
            self.assertEqual(data_parser.get_num_comments(article), return_Val, msg)
        with self.assertRaises(
            AssertionError,
            msg="Test wrong type of data"):
            data_parser.get_num_comments(5)

    """
    Tests data_parser.get_title(article)
    """
    def test_clean_up_data(self):
        list_of_assertions = [
            ({}, 
             {"title": None, "num_comments": 0}, 
             "Test empty article"),

            ({"title": "some_title"}, 
             {"title": "some_title", "num_comments": 0}, 
             "Test only title in article"),

            ({"story_title": "some_title"}, 
             {"title": "some_title", "num_comments": 0}, 
             "Test only story title article"),

            ({"title": 1, "story_title": 1, "num_comments": "a"}, 
             {"title": None, "num_comments": 0}, 
             "Test wrong type title, story_title and num_comments"),

            ({"title": 1, "story_title": "some_title", "num_comments": 5}, 
             {"title": "some_title", "num_comments": 5}, 
             "Test wrong type title"),

            ({"title": "some_title", "story_title": 1, "num_comments": 5}, 
              {"title": "some_title", "num_comments": 5}, 
              "Test wrong type story_title")
        ]
        for article, return_Val, msg in list_of_assertions:
            self.assertEqual(data_parser.clean_up_data(article), return_Val, msg)
        with self.assertRaises(
            AssertionError,
            msg="Test wrong type of data"):
            data_parser.get_title(5)
    
    """
    Tests data_parser.process_page(page)
    """
    def test_process_page(self):
        page = [
            {},
            {"title": "some_title"},
            {"story_title": "some_title"},
            {"title": 1, "story_title": 1, "num_comments": "a"},
            {"title": 1, "story_title": "some_title", "num_comments": 5},
            {"title": "some_title", "story_title": 1, "num_comments": 5}
        ] * 2
        correct = [
            {"title": "some_title", "num_comments": 0},
            {"title": "some_title", "num_comments": 0},
            {"title": "some_title", "num_comments": 5},
            {"title": "some_title", "num_comments": 5}
        ] * 2
        self.assertEqual(
            data_parser.process_page(page),
            correct,
            "Test correct filtering and cleanup of data."
        )

        with self.assertRaises(
            AssertionError,
            msg="Test wrong type of data"):
            data_parser.process_page(5)
    
    """
    Tests data_parser.get_top_10_titles_by_num_of_comments(data)
    """
    def test_get_top_10_titles_by_num_of_comments(self):
        data = []
        for i in range(101):
            data.append(
                {"title": "a"*i, "num_comments": i}
            )
        random.shuffle(data)
        top_10 = data_parser.get_top_10_titles_by_num_of_comments(data)
        top_10 = [len(e) for e in top_10]

        self.assertEqual(
            top_10,
            [i for i in range(100, 90, -1)],
            "Test correct choice of top 10"
        )

        with self.assertRaises(
            AssertionError,
            msg="Test wrong type of data"):
            data_parser.get_top_10_titles_by_num_of_comments(5)

if __name__ == '__main__':
    unittest.main()