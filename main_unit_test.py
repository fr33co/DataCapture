import unittest
from main import DataCapture


class TestDataCapture(unittest.TestCase):
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.build_stats()

    def test_less(self):
        """
        test_less: Validates that the less function returns the correct
        number of values less than 4 in the list.
        """
        self.assertEqual(self.capture.less(4), 2)

    def test_greater(self):
        """
        test_greater: Validates that the greater function returns the correct
        number of values greater than 4 in the list.
        """
        self.assertEqual(self.capture.greater(4), 2)

    def test_between(self):
        """
        test_between: Validates that the between function returns the correct
        number of values between 3 and 6 in the list.
        """
        self.assertEqual(self.capture.between(3, 6), 4)


if __name__ == '__main__':
    unittest.main()