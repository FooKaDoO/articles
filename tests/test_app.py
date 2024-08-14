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
import app

class TestApp(unittest.TestCase):

    """
    Tests app.get_all_data()
    """
    def test_get_all_data(self):
        self.assertEqual(
            app.get_all_data(),
            service.get_top10_titles(),
            "Test if app.get_all_data() returns service.get_top10_titles()"
        )

if __name__ == '__main__':
    unittest.main()