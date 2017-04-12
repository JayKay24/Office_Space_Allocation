import unittest

class OfficeTest(unittest.TestCase):
    def setUp(self):
        self.office = Office("Blue")

    def testOfficeHasMaxNum6(self):
        self.assertEqual(self.office.max_num, 6)

    def testOfficeHasAttributeName(self):
        self.assertEqual(self.office.name, "Blue")

if __name__ == "__main__":
	unittest.main()