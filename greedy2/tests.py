import unittest
from operations import change_owed


class OperationsTest(unittest.TestCase):
    def test_change_owned_minimum_value(self):
        """Should recieves minimium value"""
        self.assertEqual(change_owed(1), 1)

    def test_change_owed_nickel(self):
        """Should recieves a nickel"""
        self.assertEqual(change_owed(5), 1)

    def test_change_owed_dimes(self):
        """Should recieves a dime"""
        self.assertEqual(change_owed(10), 1)

    def test_change_owed_one_quarter(self):
        """Should recieves a quarter"""
        self.assertEqual(change_owed(25), 1)

    def test_change_owed_two_coins(self):
        """Should recieves two coins"""
        self.assertEqual(change_owed(15), 2)

    def test_change_owed_four_coins(self):
        """Should recieves four coins"""
        self.assertEqual(change_owed(41), 4)

    def test_change_owed_seven_coins(self):
        """Should recieves seven coins"""
        self.assertEqual(change_owed(160), 7)

    def test_change_owed_not_a_number(self):
        """Should recieves a non-nuumeric value"""
        self.assertEqual(change_owed('foo'), 'Invalid value')

    def test_change_owed_negative_number(self):
        """Should recieves a negative number"""
        self.assertEqual(change_owed(-1), 'Invalid value')


if __name__ == "__main__":
    unittest.main()
