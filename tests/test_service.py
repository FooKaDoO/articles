import unittest

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

import service

class TestService(unittest.TestCase):

    """
    Tests service.get_top10_titles()
    """
    def test_get_top10_titles(self):
        self.assertTrue(
            isinstance(service.get_top10_titles(), list),
            "Test if service.get_top10_titles() returns a list."
        )
        for elem in service.get_top10_titles():
            self.assertTrue(
                isinstance(elem, str),
                "Test if service.get_top10_titles() returns a list of strings."
            )

if __name__ == '__main__':
    unittest.main()