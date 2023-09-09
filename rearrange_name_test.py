from rearrange_name import rearrange_name
import unittest

class TestRearrangeName(unittest.TestCase):
     def test_surname_comma_firstname(self):
          testcase = "Boateng, Kofi"
          expected = "Kofi Boateng"
          self.assertEqual(rearrange_name(testcase), expected)

unittest.main()