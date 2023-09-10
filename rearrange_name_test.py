from rearrange_name import rearrange_name
import unittest

class TestRearrangeName(unittest.TestCase):
     def test_surname_comma_firstname(self):
          testcase = "Boateng, Kofi"
          expected = "Kofi Boateng"
          self.assertEqual(rearrange_name(testcase), expected)

     def test_empty_strings(self):
          testcase = ""
          expected = ""
          self.assertEqual(rearrange_name(testcase), expected)

     def test_double_names(self):
               testcase = "Boateng, Kofi I."
               expected = "Kofi I. Boateng"
               self.assertEqual(rearrange_name(testcase), expected)

unittest.main()