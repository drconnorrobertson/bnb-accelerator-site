import unittest
from build_tracker_proformas import display_address

class DisplayAddressTests(unittest.TestCase):
 def test_matching_duplicate_price(self):
  self.assertEqual(display_address('$399,900 115 Ridgewood Ave, Mary Esther, FL 32569','$399,900'),'115 Ridgewood Ave, Mary Esther, FL 32569')
 def test_mismatched_price_is_preserved(self):
  self.assertEqual(display_address('$399,900 115 Ridgewood Ave','$400,000'),'$399,900 115 Ridgewood Ave')
 def test_normal_address_is_preserved(self):
  self.assertEqual(display_address('115 Ridgewood Ave','$399,900'),'115 Ridgewood Ave')

if __name__=='__main__':unittest.main()
