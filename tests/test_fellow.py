import unittest
import sys

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class FellowTest(unittest.TestCase):
    def setUp(self):
        self.fellow = Fellow("James", "Kinyua", "Fellow")

    def testFellowHasOptIn(self):
        self.assertEqual(self.fellow.opt_in, False)

if __name__ == "__main__":
	unittest.main()