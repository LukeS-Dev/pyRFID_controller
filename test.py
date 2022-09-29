# Importing modules for error checking and unittest module 
import ConfigClass
import unittest
import os
from pathlib import Path


class TestConfigClass(unittest.TestCase):

    def test_file_exists(self):
        path_to_file = 'config.json'
        path = Path(path_to_file)

        a = path.is_file()
        b = True
        if a == b:
            file_exists_test_value = True
        else:
            file_exists_test_value = False
        self.assertEqual(a, b)
        return file_exists_test_value


    
# class Testing(unittest.TestCase):
#     def test_string(self):
#         a = 'some'
#         b = 'some'
#         self.assertEqual(a, b)

#     def test_boolean(self):
#         a = True
#         b = True
#         self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
