import unittest

class FellowTest(unittest.TestCase):
    def setUp(self):
        self.fellow = Fellow("James", "Kinyua", "Fellow")

    def testFellowHasOptIn(self):
        self.assertEqual(self.fellow.opt_in, False)

if __name__ == "__main__":
	unittest.main()