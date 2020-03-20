import unittest
from julioe_lambdata.my_mod import split_addresses, state_abbreviation

class TestStringMethods(unittest.TestCase):

    def test_split_addresses(self):
        x = 'Las Vegas, NV 89203'
        self.assertEqual(split_addresses(x),['Las Vegas', 'NV', '89203'])
        # check that s.split fails when the separator is not a string

    def test_state_abbreviation(self):
        y = 'California'
        self.assertEqual(state_abbreviation(y),'CA')

if __name__ == '__main__':
    unittest.main()