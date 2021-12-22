#!usr/bin/python3
""" Test console.py """
import unittest
import pep8


class tests_console(unittest.TestCase):
    """ Test Console """

    def test_pep8_conformance(self):
        """ pep8 """
        stylemodel = pep8.StyleGuide(quiet=True)
        result = stylemodel.check_files(['console.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
